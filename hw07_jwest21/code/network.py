'''
PROGRAMMER: Jakob K. West
USERNAME: jwest21
PROGRAM: network.py

DESCRIPTION: UDP Socket Programming -
Given protocol.py and manager.py complete
the python script for network.py

'''

import socket
import random
import threading
import protocol
import time


ipv4_addr = protocol.get_myIP()

setup_lock = threading.Lock()
print_lock = threading.Lock()


def tprint(s):

    print_lock.acquire()
    print(s)
    print_lock.release()


def find_manager():

    # Establish initial contact with BEACON to get port number for manager
    beacon_port = protocol.beacon_port
    
    setup_lock.acquire() # Needed to share beacon port on local_host

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipv4_addr, beacon_port))

    beacon_found = False
    while not beacon_found:
        data, addr = sock.recvfrom(4096)
        (recipient, sender, message) = protocol.depacketize(data)
        if "BEACON" == sender:
            if "MANAGER" in message:
                manager_port = int(message["MANAGER"])
                manager_addr = (addr[0], manager_port)
                beacon_found = True
    sock.close()                
    setup_lock.release()
    
    return manager_addr


def join_network(manager_address):
    
    # Use a random port number until the manager assigns a permanent one
    port = random.randrange(23000, 24000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipv4_addr, port))

    # Request a node name and port number from the manager
    node_port = -1
    while node_port < 0:
        datagram = protocol.packetize("MANAGER", "UNKNOWN", {"HELLO":''})
        sock.sendto(datagram, manager_address)
        datagram, addr = sock.recvfrom(4096)
        (recipient, sender, message) = protocol.depacketize(datagram)
        if ("USENAME" in message) and ("USEPORT" in message):
            node_name = message["USENAME"]
            node_port = int(message["USEPORT"])
    sock.close()

    return (node_name, node_port)


def router(router_number):

    forwarding_table = {}

    # Find the manager and join the network
    manager_address = find_manager()
    (node_name, node_port) = join_network(manager_address)
    
    tprint("%02d [%s] PORT: %5d" % (router_number, node_name, node_port))
    
    # Create the final socket for the router on the assigned port            
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipv4_addr, node_port))

    while True:

        # Wait for a message
        datagram, addr = sock.recvfrom(4096)
        (recipient, sender, message) = protocol.depacketize(datagram)
        
        if sender == "MANAGER":
            
            if "NEIGHBOR" in message:
                neighbor_port = message["NEIGHBOR"]
                forwarding_table[neighbor_port] = {"distance": 1} # Direct connection
                # Prepare and send LINK message
                link_msg = protocol.packetize(node_name, "UNKNOWN", {"LINK": f"{node_port}"})
                sock.sendto(link_msg, (ipv4_addr, int(neighbor_port)))
                
            elif "DUMP" in message:
                # Prepare and send TABLE message
                table_msg = {node: data for node, data in forwarding_table.items()}
                sock.sendto(protocol.packetize(node_name, "MANAGER", table_msg), manager_address)
            
            else: # Message from a neighbor
                
                if "LINK" in message:
                    neighbor_name = sender # Assuming sender name is valid
                
                if neighbor_name not in forwarding_table or forwarding_table[neighbor_name]['distance'] > 2:
                    forwarding_table[neighbor_name] = {"distance": 2} # Indirect connection via one hop
                    # Respond with a LINK message if the recipient was "UNKNOWN"
                    if recipient == "UNKNOWN":
                        response_link_msg = protocol.packetize(node_name, neighbor_name, {"LINK": f"{node_port}"})
                        sock.sendto(response_link_msg, (ipv4_addr, addr[1]))
                
                elif "EXCHANGE" in message:
                    # Processing EXCHANGE message
                    modified = False
                    for entry in message:
                        node, dist = entry.split(',')
                        dist = int(dist)
                        if node not in forwarding_table or forwarding_table[node]['distance'] > dist + 1:
                            forwarding_table[node] = {"distance": dist + 1}
                            modified = True
                            
                    # If the forwarding table was modified, send a table summary to each neighbor
                    if modified:
                        for neighbor in forwarding_table:
                            summary_msg = {node: data for node, data in forwarding_table.items()}
                            sock.sendto(protocol.packetize(node_name, "UNKNOWN", summary_msg), (ipv4_addr, int(neighbor)))
            
            
if __name__ == '__main__':
    
    nodes_in_network = 32
    threads = []
    for i in range(nodes_in_network):
        threads.append(threading.Thread(target = router, args = [i]))
    for thread in threads:
        thread.start()
        
# Jakob West
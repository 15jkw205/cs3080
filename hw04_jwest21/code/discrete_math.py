'''
PROGRAMMER: Jakob K. West
USERNAME: jwest21
PROGRAM: discrete_math.py

DESCRIPTION: Function to print large integers separated by commas
'''

import threading
import time

    
# Global variable for time expiration
time_expired = False

"""""""""""""""""""""
PRETTY INT FUNCTION
"""""""""""""""""""""

print("discrete_math.py : pretty_int() test")
print()

def pretty_int(n):
    
    """
    Convert a non-negative integer to a string with thousands separators.
    
    Parameters:
    n (int): A non-negative integer.
    
    Returns:
    str: A string representing the number with comma separators for thousands.
    """
    return '{:,}'.format(n)

try:
    pretty_int
except NameError:
    print("    Function pretty_int() not implemented")
    print()
else:
    n_list = [0, 1, 999, 1000, 2**16, 2**64]
    for n in n_list:
        print("  ", n, "=", pretty_int(n))
print()


"""""""""""""""""""""""
PRETTY FACTOR FUNCTION
"""""""""""""""""""""""

print("discrete_math.py : prime_factor() test")
print()

def prime_factor(n):
    
    """
    Find a prime factor of a number.
    
    Parameters:
    n (int): An integer to factor.
    
    Returns:
    tuple: A tuple containing two integers. The first integer is a prime factor
    of n, and the second integer is n divided by the prime factor. If the number
    is prime, then the return value is (n, 1). If the function fails to find a
    prime factor, it returns (1, n).
    """
    
    global time_expired
    
    if n < 2 or not isinstance(n, int):
        return (1, n)
    
    divisor = 2
    while divisor ** 2 <= n:
        if time_expired:
            return (1, n)
        if n % divisor == 0:
            return (divisor, n // divisor)
        divisor += 1
        
    return (n, 1)

    '''
try:
    prime_factor
except NameError:
    print("    Function pretty_factor() not implemented")
    print()
else:

    for n in [0, 1, 2, 3, 12, 97]:
        start_time = time.time()
        result = prime_factor(n)
        end_time = time.time()
        print("    %s = (%s)*(%s) ( %.3f seconds)" \
              % (pretty_int(n), pretty_int(result[0]),
                 pretty_int(result[1]), end_time - start_time))
    for n in [69_151*83_621, 1264447*3715967, 12957929*19528517, 320019647*57000000011, 61256847931289*612671]:
        start_time = time.time()
        result = prime_factor(n)
        end_time = time.time()
        print("    %s = (%s)*(%s) ( %.3f seconds)" \
              % (pretty_int(n), pretty_int(result[0]),
                 pretty_int(result[1]), end_time - start_time))
                 '''
    
    

"""""""""""""""""""""""
FACTOR THREAD FUNCTION
"""""""""""""""""""""""

def factor_thread(num, result, lock):
    
    """
    Thread target function to factor a single number and store the result.
    
    Parameters:
    num (int): The number to factor.
    result (list): A list to store the factorization result.
    lock (threading.Lock): A lock to synchronize access to the result list.
    """
    
    global time_expired
    
    # Factor the number
    prime_factors = prime_factor(num)
    
    # Acquire lock to access result list
    lock.acquire()
    
    # Store the result
    result.append((num, prime_factors))
    
    # Release lock
    lock.release()
    
    
    
"""""""""""""""""""""
FACTOR LIST FUNCTION
"""""""""""""""""""""

print("discrete_math.py : factor_list() test")
print()

def factor_list(numbers, time_limit):
    
    """
    Factor a list of numbers using threading.
    
    Parameters:
    numbers (list): A list of numbers to factor.
    time_limit (int): The time limit in seconds.
    """
    
    global time_expired
    
    # Initialize variables
    result = []
    lock = threading.Lock()
    threads = []
    
    # Start threads for factorization
    for num in numbers:
        thread = threading.Thread(target=factor_thread, args=(num, result, lock))
        thread.start()
        threads.append(thread)
        
    # Wait until time limit or all threads are finished
    start_time = time.time()
    while time.time() - start_time < time_limit and threading.active_count() > 1:
        time.sleep(0.1)
    
    # Set time_expired flag to signal threads to end
    time_expired = True
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
        
    # Print results
    print("Factoring a list of RSA numbers")
    print("List length:", len(numbers), "numbers")
    print("Time limit:", time_limit, "seconds")
    
    # Filter out trivial factorizations
    non_trivial_results = [(num, factors) for num, factors in result if factors[0] != 1]
    
    # Print non-trivial factorizations
    for num, factors in non_trivial_results:
        print(pretty_int(num), "=", pretty_int(factors[0]), "*", pretty_int(factors[1]), "--- (", "{:.3f}".format(time.time() - start_time), "sec )")
        
    # Check if time expired
    if time.time() - start_time >= time_limit:
        print("TIME EXPIRED")
        
    # Count successfully factored numbers
    successes = len(non_trivial_results)
    print("Successfully factored", successes, "numbers.")
    
    # Print aborting and cleanup messages
    print("Terminating", threading.active_count() - 1, "child threads.")
    aborted_numbers = [pretty_int(num) for num, factors in result if factors[0] == 1]
    print("Aborting:", ", ".join(aborted_numbers))
    print("Clean up complete, exiting program.")

'''
try:
    factor_list
except NameError:
    print("   Function factor_list() not implemented")
    print()
else:

    rsa_p1 = [6186493,42598097,6186503,6186527,42598099,42597899,6186611,42597917,6186619,42597871]
    rsa_p2 = [42597871,42597889,42597899,42597911,42597917,42597923,6186527,42597979,42598097,42598099]
    rsa_list = []
    for p1, p2 in zip(rsa_p1, rsa_p2):
        rsa_list.append(p1 * p2)
    factor_list(rsa_list, 8)
'''


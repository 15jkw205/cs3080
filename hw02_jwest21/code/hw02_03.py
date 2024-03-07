'''
PROGRAMMER: .... Jakob K. West
USERNAME: ...... jwest21
PROGRAM: ....... hw02_03.py

DESCRIPTION: ...
'''

import re
def extract_assembly_code(input_filename):
    output_filename = input_filename + ".asm"
    
# Open the disassembler output file for reading
with open(input_filename + ".dis", "rt") as fp:
        data = fp.read()
        
    # Define a regular expression pattern to match assembly code
    regex = re.compile(r"^\s*(?![01])[^\n]*$", re.MULTILINE)
    results = regex.findall(data)
    
    # Output file for writing
    with open(output_filename, "wt") as fp:
        for item in results:
            print(item)
            fp.write(item + "\n")

def main():
    # Input disassembler output file name
    print("DATA ENTRY")
    filename = input("Enter a disassembler output file name (w/o extension): ")
    # print the assembly code
    print("\nASSEMBLY CODE")
    extract_assembly_code(filename)
    
if __name__ == "__main__":
    main()
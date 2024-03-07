'''
PROGRAMMER: .... Jakob K. West
USERNAME: ...... jwest21
PROGRAM: ....... hw02_01.py

DESCRIPTION: Disassembling hackman
'''

# Function used to disassemble
def disassemble_instruction(instruction):
    
    if instruction.startswith('0'):
        return f"@{int(instruction[1:], 2)}"
    
    elif instruction.startswith('111'):
        comp = instruction[1:8]
        dest = instruction[8:11]
        jump = instruction[11:]
        return f"{comp_dict[comp]}={dest_dict[dest]};{jump_dict[jump]}"
    
def read_hack_file(filename):
    with open(filename + '.hack', 'r') as file:
        lines = file.readlines()
    return  [line.strip() for line in lines if line.strip()]

# Dictionary mapping comp, dest, and jump fields to their respective text strings

# Dictionary #1 - comp
comp_dict = {
    '0000000': '0',
    '0000001': '1',
    '0000010': '-1',
    '0001100': 'D',
    '0001101': 'A',
    '0001111': '!D',
    '0001110': '!A',
    '0011101': '-D',
    '0011111': '-A',
    '0011110': 'D+1',
    '0011011': 'A+1',
    '0000011': 'D-1',
    '0000111': 'A-1',
    '0001112': 'D+A',
    '0011000': 'D-A',
    '0010011': 'A-D',
    '0000110': 'D&A',
    '0010101': 'D|A',
    '1110000': 'M',
    '1110001': '!M',
    '1110011': '-M',
    '1110111': 'M+1',
    '1110010': 'M-1',
    '1111111': 'D+M',
    '1111010': 'D-M',
    '1110011': 'M-D',
    '1110000': 'D&M',
    '1110101': 'D|M'
}

# Dictionary #2 - dest
dest_dict = {
    '000': 'null',
    '001': 'M',
    '010': 'D',
    '011': 'MD',
    '100': 'A',
    '101': 'AM',
    '110': 'AD',
    '111': 'AMD'
}

# Dictionary #3 - jump
jump_dict = {
    '000': 'null',
    '001': 'JGT',
    '010': 'JEQ',
    '011': 'JGE',
    '100': 'JLT',
    '101': 'JNE',
    '110': 'JLE',
    '111': 'JMP'
}


# main method
def main():
    print("DATA ENTRY")
    filename = input("Enter the name of a .hack file: ")
    instructions = read_hack_file(filename)
    
    # Final print statements
    print("\nDISASSEMBLED OUTPUT")
    for instruction in instructions:
        print(instruction, disassemble_instruction(instruction))

if __name__ == "__main__":
    main()

    




        
        
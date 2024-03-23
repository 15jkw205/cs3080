'''
PROGRAMMER: Jakob K. West
USERNAME: jwest21
PROGRAM: hw06_01.py

DESCRIPTION: DATA MINING!!!!!
Scan the contents of a zipped-up file to
find the five-digit numbers and sum them up
'''


import re
from pathlib import Path
import zipfile


# File name variables
zip_file_name = 'data.zip'
file_name = 'data'


# Function #1
def unzip_file(zip_file):
    
    # Unzip the file
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall()


# Function #2 
def count_subdirectories(directory):
    
    # Count the number of subdirectories inside the given directory
    subdirectories = [subdir for subdir in Path(directory).iterdir() if subdir.is_dir()]
    return len(subdirectories)


# Function #3 
def count_files_in_subdirectory(subdirectory):
    
    # Count the number of files inside each subdirectory
    files = [file for file in Path(subdirectory).iterdir() if file.is_file()]
    return len(files)


# Function #4
def find_five_digit_numbers(file_path):
    
    # Find all five-digit numbers surrounded by dollar signs ($) in a file
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            numbers.extend(re.findall(r'\$(\d{5})\$', line))
            
    return numbers


# Function #5
def sum_five_digit_numbers(numbers):
    
    # Sum up all the five-digit numbers
    return sum(int(number) for number in numbers)


# Main Function
def main(zip_file):
    
    # Unzip the file
    unzip_file(zip_file)
    
    # Count subdirectories inside the file_name directory
    num_subdirectories = count_subdirectories(file_name)
    print("Number of subdirectories:", num_subdirectories)
    print()
    
    # Loop through each subdirectory
    total_num_files = 0
    total_numbers = []
    for subdir in Path(file_name).iterdir():
        if subdir.is_dir():
            
            # Count the number of files in each subdirectory
            num_files = count_files_in_subdirectory(subdir)
            total_num_files += num_files
            print(f"Number of files in {subdir}: {num_files}")
            
            # Find and append five-digit numbers to the list
            for file_path in subdir.iterdir():
                if file_path.is_file():
                    total_numbers.extend(find_five_digit_numbers(file_path))
                    
    print()
    
    # Sum up all the five-digit numbers
    total_sum = sum_five_digit_numbers(total_numbers)
    print("Total number of files:", total_num_files)
    print()
    print("Total number of five-digit numbers found:", len(total_numbers))
    print()
    print("Sum of those numbers:", total_sum)
    

if __name__ == "__main__":
    print("DATA MINING!!!", end='\n\n')
    main(zip_file_name)
    
# Jakob West
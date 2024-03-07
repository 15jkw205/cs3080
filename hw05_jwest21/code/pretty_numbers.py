'''
PROGRAMMER: Jakob K. West
USERNAME: jwest21
PROGRAM: pretty_number.py

DESCRIPTION: Module to neatly format numbers using various user-created functions
'''


def pretty_int(n, sep=',', group=3):
    """
    Convert a non-negative integer to a string with arbitrary separators.
    
    Parameters:
    n (int): A non-negative integer.
    sep (str): The separator character or string. Default is ','.
    group (int): The number of digits in each group. Default is 3.
    
    Returns:
    str: A string representing the number with specified separators and grouping.
    """
    
    
    # Round group to the nearest integer
    group = int(round(group))
    
    # Handle case when group size is 0 or less
    if group <= 0:
        return str(n)
    
    # Convert integer to string
    num_str = str(n)
    
    # Insert separators
    result = ''
    for i in range(len(num_str)):
        if i > 0 and (len(num_str) - i) % group == 0:
            result += sep
        result += num_str[i]
    
    return result


def test_pretty_int():
    """
    Test function for pretty_int.
    """
    
    test_cases = [
        (1000000, ',', 3),
        (1234567890, '-', 4),
        (9876543210, ';', 2),
        (1234567890, '.', 0),
        (1234567890, '-', 2.7),
        (9876543210, ';', -3),
        (9876543210, '->', 3),
        (9876543210, '---', 1)
    ]
    
    print("PRETTY INT FUNCTION")
    print()
    
    for n, sep, group in test_cases:
        print(f"Input: {n}, Separator: '{sep}', Group: {group}")
        try:
            result = pretty_int(n, sep, group)
            print("Output: ", result)
        except Exception as e:
            print("Error: ", e)
        print()
        
if __name__ == "__main__":
    test_pretty_int()
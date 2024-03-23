'''
PROGRAMMER: Jakob K. West
USERNAME: jwest21
PROGRAM: pretty_number.py

DESCRIPTION: Module to neatly format numbers using various user-created functions
'''


"""""""""""""""""""""
PRETTY INT FUNCTION
"""""""""""""""""""""

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
    Test function for pretty_int().
    """
    
    test_cases = [
        (320875, ';', 5),          # Test case with a large positive number and a semicolon separator with a group size of 5
        (9762, '-', 2),            # Test case with a small positive number and a hyphen separator with a group size of 2
        (54123, ',', 3),           # Test case with a medium positive number and a comma separator with a group size of 3
        (8825614, '.', 4),         # Test case with a large positive number and a period separator with a group size of 4
        (379041, '-', 3),          # Test case with a medium positive number and a hyphen separator with a group size of 3
        (86542, ',', 2),           # Test case with a medium positive number and a comma separator with a group size of 2
        (1854320, '.', 6),         # Test case with a large positive number and a period separator with a group size of 6
        (70819, ';', 4),           # Test case with a medium positive number and a semicolon separator with a group size of 4
        (963274, '-', 3),          # Test case with a large positive number and a hyphen separator with a group size of 3
        (5429, ',', 5)             # Test case with a small positive number and a comma separator with a group size of 5
    ]


    print("\nPRETTY INT FUNCTION")
    print()
    
    for n, sep, group in test_cases:
        print(f"Input: {n}, Separator: '{sep}', Group: {group}")
        try:
            result = pretty_int(n, sep, group)
            print("Output: ", result)
        except Exception as e:
            print("Error: ", e)
        print()
        
        
        
"""""""""""""""""""""
PRETTY NUM FUNCTION
"""""""""""""""""""""

def pretty_num(n, sep=',', group=3, places=6, mark='.'):
    
    """
    Convert a number to a string with arbitrary separators and decimal formatting.
    
    Parameters:
    n (float or int): The number to format.
    sep (str): The separator character or string. Default is ','.
    group (int): The number of digits in each roup Default is 3.
    places (int): The number of decimal places. Default is 6.
    mark (str): The character used as the decimal point. Default is '.'.
    
    Returns:
    str: A string representing the number with specified separators and decimal formatting.
    """
    
    # Round group to the nearest integer
    group = int(round(group))
    
    # Handle case when group size is 0 or less
    if group <= 0:
        return str(n)
    
    # Handle negative numbers
    if n < 0:
        sign = '-'
        n = abs(n)
    else:
        sign = ''
    
    # Convert to string and split integer and decimal parts
    num_str = str(n)
    integer_part, _, decimal_part = num_str.partition('.')
    
    # Insert separators for integer part
    result = ''
    for i in range(len(integer_part)):
        if i > 0 and (len(integer_part) - i) % group == 0:
            result += sep
        result += integer_part[i]
        
    # Add decimal part with specified number of places
    result += mark + decimal_part[:places]
    
    return sign + result


def test_pretty_num():
    """
    Test function for pretty_num().
    """
    
    test_cases = [
        (17348.235, ',', 3, 6, '.'),    # Random positive number with separators and decimal places
        (-9075.7689, ';', 4, 3, ','),   # Random negative number with different separators and decimal places
        (1352.47, '.', 2, 4, '.'),      # Random positive number with decimal point and specified group size
        (450987.13572, '-', 5, 5, ':'), # Random positive number with separators and decimal places
        (-36842.689, ',', 2, 7, ','),   # Random negative number with different separators and decimal places
        (123456.789, ';', 3, 2, ';'),   # Random positive number with different separators and decimal places
        (99999, '.', 0, 3, '.'),        # Random positive number with zero decimal places
        (-753.91, '-', 2, 5, ','),      # Random negative number with different separators and decimal places
        (5287.6301, ',', -3, 4, '.'),   # Random positive number with negative group size and decimal places
        (825731.45, '-', 7, 2, ':')     # Random positive number with separators and decimal places
    ]


    
    print("\nPRETTY NUM FUNCTION")
    print()
    
    for n, sep, group, places, mark in test_cases:
        print(f"Input: {n}, Separator: '{sep}', Group: {group}, Places: {places}, Mark: '{mark}'")
        try:
            result = pretty_num(n, sep, group, places, mark)
            print("Output:", result)
        except Exception as e:
            print("Error:", e)
        print()
        
        

"""""""""""""""""""""
PRETTY SF FUNCTION
"""""""""""""""""""""

def pretty_sf(n, sep=',', group=3, places=6, sigfigs=3, mark='.'):
    """
    Convert a number to a string with arbitrary separators and specified
    significant figures
    
    Parameters:
    n (float or int): The number to format.
    sep (str): The separator character or string. Default is ','.
    group (int): The number of digits in each group. Default is 3.
    places (int): The number of decimal places. Default is 6. 
    sigfigs (int): The number of significant figures. Default is 3.
    mark (str): The character used as the decimal point. Default is '.'.
    
    Returns:
    str: A string representing the number with specifed separators and significant figures.
    """
    # Check if significant figures are specified
    if sigfigs is not None:
        # Calculate the number of decimal places to round to based on significant figures
        places = max(0, sigfigs - len(str(int(abs(n)))) - (0 if n == 0 else 1))
    
    # Round the number to the specified decimal places
    rounded_num = round(n, places)
    
    # Convert the rounded number to a string with the desired format
    formatted_str = '{:.{places}f}'.format(rounded_num, places=max(0, places))
    
    # Insert separators
    result = ''
    decimal_index = formatted_str.index('.')
    for i in range(len(formatted_str)):
        if formatted_str[i] == '.':
            result += mark
            
        else:
            result += formatted_str[i]
            if i < decimal_index and (decimal_index - i - 1) % group == 0 and i != decimal_index - 1:
                result += sep
    
    return result
        


def test_pretty_sf():
    """
    Test function for pretty_sf.
    """
    test_cases = [
        (0.56342897, ',', 4, 6, 3, '.'),       # Random positive number with separators and 6 significant figures
        (-987.2176098, '-', 3, 4, 2, ','),     # Random negative number with different separator and 4 significant figures
        (123456.789124, ';', 5, 7, 4, ':'),    # Random large positive number with different separator and 7 significant figures
        (654.93786, '.', 0, 3, 5, '.'),        # Random positive number with no decimal places and 3 significant figures
        (-0.43521678, '-', 2.5, 5, 3, ','),    # Random negative number with non-integer group size and 5 significant figures
        (1234567890.123, ',', -4, 4, 6, ';'),   # Random large positive number with negative group size and different separator
        (0.98654321, '.', 2, 6, 4, '.'),       # Random small positive number with 2 decimal places and 6 significant figures
        (-0.12456789, ';', 5, 6, 3, ','),      # Random negative number with different separator and 6 significant figures
        (456.793210, ',', 6, 3, 2, '.'),       # Random positive number with different group size and 3 significant figures
        (-87654321.098, '-', 4, 4, 4, ':')     # Random negative number with different separator and 4 significant figures
    ]


    
    print("\nPRETTY SF FUNCTION")
    print()
    
    for n, sep, group, places, sigfigs, mark in test_cases:
        print(f"Input: {n}, Separator: '{sep}', Group: {group}, Places: {places}, Sigfigs: {sigfigs}, Mark: '{mark}'")
        try:
            result = pretty_sf(n, sep, group, places, sigfigs, mark)
            print("Output:", result)
        except Exception as e:
            print("Error:", e)
        print()
        


"""""""""""""""""""""
PRETTY SI FUNCTION
"""""""""""""""""""""
def pretty_si(n, sep=',', group=3, sigfigs=3, mark='.', si=False, units=''):
    """
    Convert a number to a string with SI prefix scaling and significant figures.
    
    Parameters:
    n (float or int): The number to format.
    sep (str): The separator character or string. Default is ','.
    group (int): The number of digits in each group. Default is 3.
    sigfigs (int): The number of significant figures. Default is 3.
    mark (str): The character used as the decimal point. Default is '.'.
    si (bool): If True, scale the value using SI prefixes. Default is False.
    unit (str): The units of the value. Default is ''.
    
    Returns:
    str: A string representing the number with SI prefix scaling and
    significant figures.
    """
    
    
    # Round group to the nearest integer
    group = int(round(group))
    
    # Handle case when group size is 0 or less
    if group <= 0:
        return str(n)
    
    # Handle negative numbers
    if n < 0:
        sign = '-'
        n = abs(n)
    else:
        sign = ''
        
    # Handle special case for zero
    if n == 0:
        return '0'
    
    # Convert to string
    num_str = str(n)
    
    # Determine the number of digits before the decimal point
    if '.' in num_str:
        digits_before_decimal = len(num_str.split('.')[0])
    else:
        digits_before_decimal = len(num_str)
        
    # Determine the number of digits after the decimal point
    if '.' in num_str:
        digits_after_decimal = len(num_str.split('.')[1])
    else:
        digits_after_decimal = 0
        
    # Calculate the number of significant digits
    if digits_before_decimal > 1:
        sf_count = digits_before_decimal
    else:
        sf_count = digits_before_decimal + digits_after_decimal
        
    # Determine the number of digits to remove
    remove_count = sf_count - sigfigs
    
    # Round the number to the specified significant figures
    rounded_num = round(n, remove_count)
    
    # Convert the rounded number to string
    rounded_str = str(rounded_num)
    
    # Format the string with separators
    result = ''
    for i in range(len(rounded_str)):
        if rounded_str[i] == '.':
            result += mark
        else:
            result += rounded_str[i]
            if (len(rounded_str) -i - 1) % group == 0 and i != len(rounded_str) - 1:
                result += sep
    
    # Append SI prefix and units if specified
    if si:
        prefixes = ['q', 'r', 'y', 'z', 'a', 'f', 'p', 'n', 'µ', 'm', '',
                    'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y', 'R', 'Q']
        exp_index = 10
        while exp_index < 21 and rounded_num >= 1000:
            rounded_num /= 1000
            exp_index += 1
        while exp_index > 0 and rounded_num < 1:
            rounded_num *= 1000
            exp_index -= 1
            
        prefix = prefixes[exp_index]
        if prefix:
            result += ' ' + prefix
        if units:
            result += ' ' + units
        elif units:
            result += ' ' + units
        
        return sign + result
    

def test_pretty_si():
    """
    Test Function for pretty_si.
    """
    
    test_cases = [
        (0.001234, ',', 3, 2, '.', False, ''),       # Random small positive number with no SI prefix and no units
        (-4000000, '-', 4, 3, ',', True, 'm'),       # Random large negative number with SI prefix 'M' and units 'm'
        (0.000987, ';', 2, 1, ':', False, ''),       # Random small positive number with no SI prefix and no units
        (543210987, '.', 0, 4, '-', True, 'A'),      # Random large positive number with SI prefix 'M' and units 'A'
        (7654.32, '-', 2, 3, ',', False, ''),        # Random positive number with no SI prefix and no units
        (-5678.9012, ',', 3, 2, '.', True, 'g'),     # Random negative number with SI prefix 'm' and units 'g'
        (3210987, ';', 4, 1, ':', False, ''),        # Random positive number with no SI prefix and no units
        (-0.007654, '.', 6, 3, '-', True, 'Hz'),     # Random small negative number with SI prefix 'm' and units 'Hz'
        (98765432, '-', 5, 4, ',', False, ''),       # Random large positive number with no SI prefix and no units
        (0.002345, ',', 2, 2, '.', True, 'N')        # Random small positive number with SI prefix 'm' and units 'N'
    ]

    
    print("\nPRETTY SI FUNCTION")
    print()
    
    for n, sep, group, sigfigs, mark, si, units in test_cases:
        print(f"Input: {n}, Separator: '{sep}', Group: {group}, Sigfigs: {sigfigs}, Mark: '{mark}', SI: {si}, Units: {units}")
        try:
            result = pretty_si(n, sep, group, sigfigs, mark, si, units)
            print("Output:", result)
        except Exception as e:
            print("Error:", e)
        print()
        
        
"""
Main
"""
        
if __name__ == "__main__":
    test_pretty_int()
    test_pretty_num()
    test_pretty_sf()
    test_pretty_si()
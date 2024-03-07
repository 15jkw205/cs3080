'''
PROGRAMMER: Jakob K. West
USERNAME: jwest21
PROGRAM: hx01_review.py

DESCRIPTION: Review for Midterm #1 
'''

'''
Problem #1
What is the ouptut of the following Python script?
'''

v = 42
s = ""
for i in range(10, 6, -2):
    v += 2 * i
    s += "%d" % (v)
print(s)


'''
Problem #2
When the following Python script is executed, it produces the output shown.
What change can be made to get the script to work properly?



v = -1

while not 10 <= v <= 20:
    v = input("Enter a value between 10 and 20 (inclusive: ")
print("The value you entered was %d" % (v))

# turn v into an int
'''

'''
Problem #3
The Collatz sequence for positive integer n is a sequence of integers with n such
that if n is even, the next number in the sequence is n/2, otherwise the next number
is 3n+1. The length of the Collatz sequence for n is the shortest length of the sequence,
starting with n, that includes the value 1. For example, the Collatz sequence for n=3 is

[3, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1 ...] and therefore it has a length of 8.
Write a recursive function, collatz_length(n), that returns the length of the Collatz
sequence for n. If you write a correct, but iterative function, you will receive 80% credit
for the problem.
'''


def collatz_length(n):
    
    if (n == 1):
        return 1
    
    elif (n % 2 == 0):
        return 1 + collatz_length(n / 2)
        
    else:
        return 1 + collatz_length(3 * n + 1)
    

collatz_number = int(input("Enter a positive integer to find the Collatz length: "))
print("The length of the Collatz sequence for %d:" % (collatz_number))
print(collatz_length(3))
    
    
'''
Problem #4
Python supports several data types that are "collections." Among these are lists,
sets, and tuples. Briefly describe each of these, making particular note of how
each is different from the others.
'''
# Lists: Mutable, ordered collection of items. Allows duplicate elements.
# Accessed by index.

# Sets: Mutable, unordered collection of unique items. Does not allow duplicate
# elements.

# Tuples: Immutable, ordered collection of items. Allows duplicate elements.
# Accessed by index.


'''
Problem #5
The Fibonacci sequence may be defined such that the first two values. F_0 and
F_1, are 0 and 1 while all subsequenct values are the sum of the prior two values. While
a recursive implementation of a function that returns F_n, given n, is simple, it is also
extremely inefficient (it runs in exponential time).

Write an iterative version of fib(n) that returns F_n. You may assume only valid values of n
will be passed to the function (i.e., no need to validate the input).
'''

def fib(n):
    if n <= 1:
        return n
    
    else:
        a, b = 0, 1
        
        for _ in range(2, n + 1):
            
            a,b = b, a + b
            
        return b


'''
Problem #6
For the following code snippet, what value will be stored in x?
'''

x = round(1234567.89, -2)
# 1234600.0
print(x)


'''
Problem #7
Consider the following script that is intended to print out a list of numbers from 1 thru
2 in increments of 0.2


x = 1
increment = 0.2
while x != 2:
    print("%3.2f" % (x))
    x += increment
print(x)


When run, the script does not stop. The beginning of the print output is shown below.
1.00\n1.20\n1.40\n1.60\n1.80\n2.00\n2.20\n2.40\n2.60\...

What is the reason that this script is not behaving as intended?

# Floating-point arithmetic precision leads to x not being exactly equal to 2.
# Due to this imprecision, the while loop doesn't terminate as expected.
'''

'''
Problem #8
A python scipt contains a dictionary named 'nicknames' that uses a name, such as 'Robert',
as the key and a nickname, such as "Bob' as the value. The user is asked to enter a name and,
if that name is in the  dicitionary, it prints a message giving the nickname, otherwise, it
asks the user for a nickname and adds it to the dictionary. For this problem, a given name
only has one nickname.

nicknames = {'Robert':'Bob', 'William':'Bill', 'Christina':'Chris'}
name = input("Enter a first name: ")
# YOUR CODE GOES HERE
print(nicknames)

Write the missing code such that the program behaves as follows for the two possible cases:
'''

nicknames = {'Robert':'Bob', 'William':'Bill', 'Christina':'Chris'}
name = input("Enter a first name: ")
if name in nicknames:
    print(f"A nickname for \"{name}\" is {nicknames[name]}")
else:
    nickname = input(f"Enter the nickname for \"{name}\": ")
    nicknames[name] = nickname
print(nicknames)


'''
Problem #9
The values of two resistors, R1 and R2, placed in parallel is given by the formula
R_eq = (R1 * R2) / (R1 + R2)

What value will be stored in R_eq for the following Python code snippet?
'''

R1 = 1000
R2 = 1000
Req = R1 * R2 / R1 + R2
print(Req)
'''
Problem #10
Phone numbers often use words instead of numbers, such as 1-800-FLOWERS. This is possible
because each letter in the English alphabet is mapped to a specific digit, starting with
'ABC' all mapping to 2 and 'WXYZ' all mapping to 9. Other than 9, the only digit that has
4 letters mapped to it is 7 ('PQRS'). The digits 0 and 1 have no letters and all other have
three.

Write a Python function that accepts a string, such as "1-800-FLOWERS", and returns a string
with the letters (which may be either upper or lower case) replaced with the corresponding
digits. For this example, the string returned should be "1-800-3569377".
'''

def phone_letters_to_digits(phone_number):
    mapping = {'ABC': '2', 'DEF': '3', 'GHI': '4', 'JKL': '5', 'MNO': '6', 'PQRS': '7',
               'TUV': '8', 'WXYZ': '9'}
    digits = ''
    for char in phone_number:
        for key, value in mapping.items():
            if char.upper() in key:
                digits += value
                break
        else:
            digits += char
    return digits

print(phone_letters_to_digits("1-800-FLOWERS"))



        
    
        
    
    


# Jakob West
# Exam 2 Review
# April 3rd, 2024


"""
MULTIPLE CHOICE
"""

# 1
'''
Which of the following terms describes the situation in which the
final result depends on the exact order in which executing threads get
scheduled to run?
'''
# Race Condition


# 2
'''
Which module is typically imported when a Python script needs to capture
command-line arguments passed to it by the operating system?
'''
# sys


# 3
'''
Which of the following serves as a reasonable description of a list
comprehension?
'''
# List comprehensions are a shorthand syntax for creating new lists
# based on values in an existing list


# 4
'''
Which module can be used to enable the ability to parse-command line
options and parameters as commonly used in Unix/Linux programns?
'''
# getopt


# 5
'''
Which of the following terms describes a programming task characterized
by significant interaction with slow or shared resources?
'''
# I/O bound


# 6
'''
Which of the following terms descibes a programming task dominated by
long, complicated data processing steps?
'''
# Compute bound


# 7
'''
Which of the following is NOT an advantage of multithreading in Python?
'''
# It speeds up overall program execution by assigning different threads
# to different processor cores.


# 8
'''
Which of the following is a method by which multiple threads can read
from and write to common variables without encountering problems related
to the fine details of when each thread gets scheduled to run?
'''
# Using a lock object to control when each thread may access the variable


# 9
'''
In Python, what is the major advantage of multiprocessing over
multithreading?
'''
# Multiple processes will take advantage of available processor cores,
# while multiple threads take turns using a single processor core.


# 10
'''
If three arguments are passed to a script on the command line, how long
is the argv variable that captures them?
'''
# 3 (argv is a list of strings, one for each argument).


# 11
'''
Which of the following terms describes a design pattern that allows you
to modify the functionality of a function by wrapping it in another
function?
'''
# decorator


# 12
'''
Which of the following statements is true regarding functions in Python?
'''
# Functions may be passed as arguments to another function and may return
# functions to the caller


# 13
'''
Which of the following is the syntax for a list comprehension?
'''
# newlist = [exp for item in iterable if condition == True]


# 14
'''
Which of the following is true regarding condition expressions (e.g., x
if y else z) if the 'else z' portion is omitted?
'''
# The expression always evaluates to x.


# 15
'''
Which module have we discussed that allows a Python script to access
directory/folder information and navigate through it?
'''
# pathlib



"""
LONG ANSWER
"""

# 16
'''
What output will the following Python script produce
'''
print([n for n in range(20) if n%7 == 3])
# Output --> [3, 10, 17]


# 17
'''
What output will the following Python script produce?
'''
print([int(n/2) if n%2==0 else int(3*n+1) for n in range(1,5)])
# Output --> [4, 1, 10, 2]


# 18
'''
Giving the following code, write a list comprehension (that would repace
the comment) that results in b being a list consisting of the two-digit
numbers in the list 'a' that start with a 1.
'''
a = [12, 17, 4, 34, 9, 12, 3, 29]
b = [num for num in a if num >= 10 and num < 100 and str(num).startswith('1')]
print(b)
# Output --> [12, 17, 12]


# 19
'''
What output will the following Python script produce
'''
def f1(x, y): return x + y
def f2(x,y): return x * y
def calc(f, v1, v2):
    return f(v1, v2)
print(calc(f1, 10, 12))
print(calc(f2, 10, 12))
# Output --> 22\n120


# 20
'''
What output will the following Python script produce?
'''
def f3(f,x):
    def nf():
        return '=' + str(f(x)) + '='
    return nf

my_f = f3(round, 3.14159)
print(my_f())
# Output --> =3=


# 21
def sarg(func):
    def inner(first, second):
        return func(second, first)
    return inner

@sarg
def recip(num, den):
    return round(num / den, 2)
print(recip(12,3))
# Output --> 0.25


# 22
'''
What output will the following Python script produce?
'''
x,y,z = (12,4,3)
print(x if y*z == x else y if y > z else z)
# Output --> 12


# 23
'''
In the following script, consider all possible permutations(orderings) of
the elements in the tuple (hint - there are six). How many of them
produce 12 as a result?
'''
x,y,z = (12,4,3)
print(x if y*z == x else y if y > z else z)
# There are 4 permutations that produce 12 as the result: (12,4,3),
# (4,12,3), (3,4,12), (3,12,4).


# 24
'''
By changing either the 12 or the 3 (not both) in the following script to
something other than 4, get it produce 4 as the output.
'''
x,y,z = (12,4,2)
print(x if y*z == x else y if y > z else z)
# Output --> 4


# 25
'''
What output will the following Python script produce?
'''
a = range(10,14)
b = range(20,24)
sum = 0
for (x,y) in zip(a,b):
    if x+y < 35:
        sum += x
print(sum)
# Output --> 33


# 26
'''
Consider the following Python script then replace the code between the
two comment lines with an equivalent list comprehension
'''
'''
a = range(10,15)
b = range(20,25)
s = [x*y for (x,y) in zip(a,b) if x+y < 35]
print(sum(s))
'''


# 27
'''
Given two-equal length lists, m and n, of positive integers, write a list
comprehension that produces a list containing all pairs of elements
(i.e., a list of 2-tuples) in which the element from m is a multiple of
the element from n.
'''
m = [2, 4, 6]
n = [1, 3, 2]
result = [(x, y) for x in m for y in n if x % y == 0]
print(result)
# Output --> [(2, 1), (2, 2), (4, 1), (4, 2), (6, 1), (6, 3), (6, 2)]


# 28
'''
Given a list, s, of strings, write a list comprehension that produces a
list consisting of all strings equal in length to the first string.
'''
s = ["apple", "banana", "cherry"]
result = [string for string in s if len(string) == len(s[0])]
print(result)


# 29
'''
Given a list, s, of strings, write a list comprehension that produces a
list consisting of all subsequent strings equal in length to the first
string (the first string should only appear in the new list if it happens
to be repeated elsewhere in the list).
'''
s = ["apple", "banana", "cherry", "apricot", "blueberry"]
result = [string for string in s[1:] if len(string) == len(s[0])]
print(result)


# 30
'''
Given a list, s, of strings, write a list comprehension that produces a
list consisting of all strings that are not the same length as the first
string.
'''
s = ["apple", "banana", "cherry", "apricot", "blueberry"]
result = [string for string in s if len(string) != len(s[0])]
print(result)
      
      

# Without list comprehension
def extract_multiples_of_d(a_list, d):

    new_list = []
    for n in a_list:
        new_list.append(n)
    return new_list

# Without list comprehension
def extract_multiples_of_d_comp(a_list, d):
    return [n for n in a_list if n % d == 0]

def gcd(m, n):

    if n == 0:
        return m
    return gcd(n, m%n)

def is_coprim(m, n):
    return gcd(m, n) == 1

def pause():
    print()
    input("ENTER to continue")
    print()

if __name__ == '__main__':

    a = gen_random_list_of_integers(0, 1000, 20)

    print("Without list comprehension")
    b = extract_multiples_of_d(a, 5)
    print(f"Length of a is {len(a)}, length of b is {len(b)}")
    print(a)
    print(b)
    print()
    pause()

# Get the relative path of the current file

file=Path(__file__)
print(f"This file: {file}")
pause()

#

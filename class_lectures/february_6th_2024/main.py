"""
def myroot(x, root=2):
    y = x **(1/root)
    return y

value = int(input("Enter a number: "))

print("The square root of %f is %f" % (value, myroot(value, 3)))
print("The square root of %f is %f" % (value, myroot(value)))


def func(x, y=10):
    answer = x + y - z
    return answer

z = 10
value = func(42)
print(value, z)
"""

def multi(x):
    return(2*x, 3*x)

y = multi(20)
print(y)

a=y[0]
b=y[1]
print(a, b)

c,d = multi(30)
print(c,d)

def func2():
    print(func2)

g = func2(2)






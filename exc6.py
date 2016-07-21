"""
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
"""

def sum(l):
    t = 0
    for n in l:
        t += n
    return t

def multiply(l):
    t = 1
    for n in l:
        t *= n
    return t

n = [1, 2, 3, 4]

print sum(n)
print multiply(n)


"""
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
"""

def check_vowel(c):
    if c in "AEIOUaeiou":
        return True
    else:
        return False

print check_vowel('a')

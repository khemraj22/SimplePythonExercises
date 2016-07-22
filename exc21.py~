# -*- coding: utf-8 -*-
"""
Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab")
"""

def char_freq(str):
    myDict = {}
    t = ""
    for c in str:
        if c not in t:
            t += c
            myDict[c] = 1            
        else:
            myDict[c] += 1
    return myDict

print char_freq("stringing")

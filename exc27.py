# -*- coding: utf-8 -*-
"""
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions.
"""

def map_words(words_list):
    t = []
    map(lambda x : t.append(len(x)), words_list) 
    
  
    t1 = [len(x) for x in words_list]
    
    return t, t1
    
print map_words(["abc", "abcs", "a","abcde"])

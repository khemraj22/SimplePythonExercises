# -*- coding: utf-8 -*-
"""
Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
"""

def filter_long_words(words_list, n):
    
    return filter(lambda words_list: len(words_list)>n , words_list)

print filter_long_words(["abd123456", "aregd", "fdff", "faeyhrf"], 4)

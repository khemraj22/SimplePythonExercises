# -*- coding: utf-8 -*-
"""
Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards from English into Swedish. Use the higher order function map() to write a function translate() that takes a list of English words and returns a list of Swedish words.
"""

def translate(eng_words):
    swedish_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}   

    return map(lambda x: swedish_dict[x], eng_words)


print translate(["merry", "christmas"])

# -*- coding: utf-8 -*-
"""
Represent a small bilingual lexicon as a Python dictionary in the following fashion
 {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and 
 use it to translate your Christmas cards from English into Swedish. 
 That is, write a function translate() that takes a list of English words and returns a list of Swedish words.
"""

def translate(myList):
    myDict = {"merry":"god", 
                "christmas":"jul", 
                "and":"och", 
                "happy":"gott", 
                "new":"nytt", 
                "year":"år"}    
    newList = []
    for word in myList:
        newList.append(myDict[word])
    
    return newList
    
       
print translate(["merry", "christmas", "and", "happy", "new", "year"])   

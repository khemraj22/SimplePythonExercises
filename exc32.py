# -*- coding: utf-8 -*-
"""
Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome.
"""

#f_name = raw_input("Enter file name: ")

myfile = open("test.txt","r")
data = ""
lines = myfile.readlines()
for line in lines:

    data = line.strip();
    r = line.strip()[::-1]
        
    print r
    print len(data)
    print len(r)
    
    if data == r:
        print data
    
    

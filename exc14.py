"""
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.

"""

def map_list(word):
    num_list=[]
    for w in word:
        t = 0
        for n in w:
            t += 1
            
        num_list.append(t)
        print t
    return num_list
    
l = raw_input("enter: ").split(",")

print map_list(l)

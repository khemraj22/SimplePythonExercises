"""
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

"""

def find_longest_word(words_list):
    longest_word = []
    for word in words_list:        
        t = 0
        for n in word:
            t += 1            
        longest_word.append(t)
        
    long_word = longest_word[0]
    for n in longest_word:
        
        if long_word < n:
            long_word = n
        
    return long_word

print find_longest_word(["abcd", "EWTTFE", "Ffdsfds", "d", "erfdb", "fd", "123456789"])

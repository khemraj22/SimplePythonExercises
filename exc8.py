"""
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True """


def is_palindrome(s):
    t = ""
    for c in range(len(s)-1, -1, -1):
        t += s[c]
       
    if s == t:
        return True
    else:
        return False
        
        
print is_palindrome("n2oo2n")   

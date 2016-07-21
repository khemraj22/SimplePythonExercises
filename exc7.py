"""Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I". """

def reverse(s):
    t = ""
    for c in range(len(s)-1, -1,-1):      
       t += s[c]
    return t
    
print reverse("String123")


    

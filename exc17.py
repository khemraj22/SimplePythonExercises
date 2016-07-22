"""
Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored
"""

def palindrome_recognizer(str):
    out = "".join(c for c in str if c not in ('!','.',':','?',' '))
    t = ""
    for i in range(len(out)-1, -1, -1):
        t += out[i]
    
    out = out.lower()
    t = t.lower()
        
    if out == t:
        return "String is Palindrom"
    else:
        return "String is not Palindrom"

print palindrome_recognizer("Was it a rat I saw?")

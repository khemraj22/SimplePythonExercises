"""
Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.) """


def is_member(n, l):
    
    for v in l:
        
        if n == v:
            return True
    
    return False
        
a_list = ["ADF","abc", "bgg"] #[1,3,4,5]
a_value = "abc" #2

print is_member(a_value, a_list)

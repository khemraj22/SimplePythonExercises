"""Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to the screen.
"""

def char_freq_table():
    #f_name = raw_input("Enter file name: ")
    d= {}
    myfile = open("test.txt","r")
    
    data = myfile.read()
    s = ""
    dt = ''.join(sorted(data))
    print dt
    for c in dt:
        t = c.strip().replace("\n","")
        print c, t
        """if t not in s:
            s += t
            d[t] = 1
        #else:
            #d[t] += 1
        """
        d[t] = dt.count(t)
    print d    
        
char_freq_table()

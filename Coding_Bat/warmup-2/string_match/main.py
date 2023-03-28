'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
'''

def string_match(a,b):
    end = len(a) -1
    c = 0

    for i in range(end):
        t1, t2 = a[i:i+2], b[i:i+2]
        if t1 == t2:
            c += 1
    return c

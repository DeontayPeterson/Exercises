"""
Given a string, return the count of the number of times that a substring length 2 appears in the string
and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
"""

def last2(str):
    s = str[0:-2]
    c = 0
    for i in range(len(str)-2):
        temp = str[i:i+2]
        if s == temp:
            c += 1
    return c

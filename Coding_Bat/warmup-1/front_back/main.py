'''Given a string, return a new string where the first and last chars have been exchanged.'''

def front_back(str):
    if len(str) <= 1:
        return str
    else:
        f = str[0]
        l = str[-1]
        m = str[1:-1]

    return l + m + f
    
'''
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
'''
def hello_name(name):
    return 'Hello ' + name + "!"

# doesn't accept F strings. The following would be much easier..

def hello_name_v2(name):
    return f"Hello {name}!"
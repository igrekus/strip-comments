from strip_comments import strip

source = '''Python
Inline comments in Python use the hash ('#') character, as in the two examples in this code:

# This program prints "Hello World" to the screen
print("Hello World!")  # Note the new syntax
Block comments, as defined in this article, don't technically exist in Python.[49] A bare string literal represented by a triple-quoted string can be used[50] but is not ignored by the interpreter in the same way that "#" comment is. In the examples below, the triple double-quoted strings act in this way as comments, but are also treated as docstrings:

"""
Assuming this is file mymodule.py, then this string, being the
first statement in the file, will become the "mymodule" module's
docstring when the file is imported.
"""

class MyClass(object):
    """The class's docstring"""

    def my_method(self):
        """The method's docstring"""

def my_function():
    """The function's docstring"""
'''

expected = '''Python
Inline comments in Python use the hash ('#') character, as in the two examples in this code:


print("Hello World!")  
Block comments, as defined in this article, don't technically exist in Python.[49] A bare string literal represented by a triple-quoted string can be used[50] but is not ignored by the interpreter in the same way that "#" comment is. In the examples below, the triple double-quoted strings act in this way as comments, but are also treated as docstrings:



class MyClass(object):
    

    def my_method(self):
        

def my_function():
    
'''


def test_strips_python():

    assert strip.strip(source, language='python') == expected

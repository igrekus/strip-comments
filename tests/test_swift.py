from strip_comments import strip

source = '''Swift
Single-line comments begin with two forward-slashes (`//`):

// This is a comment.
Multiline comments start with a forward-slash followed by an asterisk (`/*`) and end with an asterisk followed by a forward-slash (`*/`):

/* This is also a comment
 but is written over multiple lines. */
Multiline comments in Swift can be nested inside other multiline comments. You write nested comments by starting a multiline comment block and then starting a second multiline comment within the first block. The second block is then closed, followed by the first block:

/* This is the start of the first multiline comment.
 /* This is the second, nested multiline comment. */
 This is the end of the first multiline comment. */
'''

expected = '''Swift
Single-line comments begin with two forward-slashes (`//`):


Multiline comments start with a forward-slash followed by an asterisk (`/*`) and end with an asterisk followed by a forward-slash (`*/`):

Multiline comments in Swift can be nested inside other multiline comments. You write nested comments by starting a multiline comment block and then starting a second multiline comment within the first block. The second block is then closed, followed by the first block:

'''


def test_strips_swift():

    assert strip.strip(source, language='swift') == expected

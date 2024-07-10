import strip_comments.strip as strip

source = '''#!/bin/cat
Hello world!
'''

expected = '''
Hello world!
'''


def test_strips_shebang():

    assert strip.strip(source, language='shebang') == expected

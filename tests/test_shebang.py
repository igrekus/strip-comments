from strip_comments import strip

source = '''#!/bin/cat
Hello world!
'''

expected = '''
Hello world!
'''


def test_strips_shebang():

    assert strip.strip(source, language='shebang') == expected

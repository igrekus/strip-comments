from strip_comments import strip

source = '''⍝ Now add the numbers:
c←a+b ⍝ addition
'''

expected = '''
c←a+b 
'''


def test_strips_apl():
    assert strip.strip(source, language='apl', preserve_newlines=True) == expected

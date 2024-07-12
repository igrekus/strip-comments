from strip_comments import strip


def test_strip_generic():
    sample = 'No <!-- I should be gone-->comment'
    actual = strip.strip(sample, language='html')

    assert actual == 'No comment'


def test_not_strip_inside_quotes():
    sample = 'No "<!-- I should NOT be gone-->"comment'
    actual = strip.strip(sample, language='html')

    assert actual == sample


def test_not_strip_comment_parts_inside_quotes():
    source = '''12.1.6 Comments
Comments must have the following format:

The string "<!--".
Optionally, text, with the additional restriction that the text must not start with the string ">", nor start with the string "->", nor contain the strings "<!--", "-->", or "--!>", nor end with the string "<!-".
The string "-->".

The text is allowed to end with the string "<!", as in <!--My favorite operators are > and <!-->.
'''

    expected = '''12.1.6 Comments
Comments must have the following format:

The string "<!--".
Optionally, text, with the additional restriction that the text must not start with the string ">", nor start with the string "->", nor contain the strings "<!--", "-->", or "--!>", nor end with the string "<!-".
The string "-->".

The text is allowed to end with the string "<!", as in .
'''

    assert strip.strip(source, language='html') == expected


def test_strip_multiline():
    source = '''<p>text</p>
<!--
first line
second line
third line
-->
<p>More text</p>
<!--
first line
second line
third line
-->
'''

    expected = '''<p>text</p>

<p>More text</p>

'''

    assert strip.strip(source, language='html') == expected


def test_strip_comments_with_only_dashes():
    source = '''All
<!---->
<!----->
<!------>
<!------->
<!-------->
<!--------->
<!---------->
<!----------->
<!------------>
<!------------->
<!-------------->
<!--------------->
<!---------------->
<!----------------->
<!------------------>
Gone
<!-- Hello -->
<!-- Hello -- -- Hello-->
<!---->
<!------ Hello -->
<!>
'''
    expected = '''All















Gone




<!>
'''

    assert strip.strip(source, language='html') == expected

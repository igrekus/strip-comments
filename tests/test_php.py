from strip_comments import strip

source = '''PHP supports 'C', 'C++' and Unix shell-style (Perl style) comments. For example:

<?php
    echo 'This is a test'; // This is a one-line c++ style comment
    /* This is a multi line comment
       yet another line of comment */
    echo 'This is yet another test';
    echo 'One Final Test'; # This is a one-line shell-style comment
?>
The "one-line" comment styles only comment to the end of the line or the current block of PHP code, whichever comes first. This means that HTML code after `// ... ?>` or `# ... ?>` WILL be printed: ?> breaks out of PHP mode and returns to HTML mode, and `//` or `#` cannot influence that. If the asp_tags configuration directive is enabled, it behaves the same with `// %>` and `# %>`. However, the </script> tag doesn't break out of PHP mode in a one-line comment.

<h1>This is an <?php # echo 'simple';?> example</h1>
<p>The header above will say 'This is an  example'.</p>
'C' style comments end at the first `*/` encountered. Make sure you don't nest 'C' style comments. It is easy to make this mistake if you are trying to comment out a large block of code.

<?php
 /*
    echo 'This is a test'; /* This comment will cause a problem */
 */
?>
'''

expected = '''PHP supports 'C', 'C++' and Unix shell-style (Perl style) comments. For example:

<?php
    echo 'This is a test'; 
        echo 'This is yet another test';
    echo 'One Final Test'; 
?>
The "one-line" comment styles only comment to the end of the line or the current block of PHP code, whichever comes first. This means that HTML code after `// ... ?>` or `# ... ?>` WILL be printed: ?> breaks out of PHP mode and returns to HTML mode, and `//` or `#` cannot influence that. If the asp_tags configuration directive is enabled, it behaves the same with `// %>` and `# %>`. However, the </script> tag doesn't break out of PHP mode in a one-line comment.

<h1>This is an <?php ?> example</h1>
<p>The header above will say 'This is an  example'.</p>
'C' style comments end at the first `*/` encountered. Make sure you don't nest 'C' style comments. It is easy to make this mistake if you are trying to comment out a large block of code.

<?php
 ?>
'''


def test_strips_php():

    assert strip.strip(source, language='php') == expected

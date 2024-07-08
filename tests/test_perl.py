import strip


source = '''# A simple example
#
my $s = "Wikipedia"; # Sets the variable s to "Wikipedia".
print $s . "\n";     # Add a newline character after printing
'''

expected = '''

my $s = "Wikipedia"; 
print $s . "\n";     
'''


def test_strips_perl():

    assert strip.strip(source, language='perl') == expected

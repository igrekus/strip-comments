import strip_comments.strip as strip

source = '''Ruby
Comments in Ruby.

Single line commenting: (line starts with hash "#")

puts "This is not a comment"

# this is a comment

puts "This is not a comment"
Multi-line commenting: (comments goes between keywords "begin" and "end")

puts "This is not a comment"

=begin

whatever goes in these lines

is just for the human reader

=end

puts "This is not a comment"
'''

expected = '''Ruby
Comments in Ruby.

Single line commenting: (line starts with hash "#")

puts "This is not a comment"



puts "This is not a comment"
Multi-line commenting: (comments goes between keywords "begin" and "end")

puts "This is not a comment"



puts "This is not a comment"
'''


def test_strips_ruby():

    assert strip.strip(source, language='ruby') == expected

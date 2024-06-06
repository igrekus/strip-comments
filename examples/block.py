import strip
s = strip.block('const foo = "bar";// this is a comment\n /* me too */')
print(s)  # => 'const foo = "bar";// this is a comment'

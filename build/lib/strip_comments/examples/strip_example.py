import strip_comments.strip as strip

s = strip.strip('const foo = "bar";/* me too */\n// this is a comment')
print(s)  # => 'const foo = "bar";\n'

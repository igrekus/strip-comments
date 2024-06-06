from strip import strip

s = strip('const foo = "bar";/* me too */\n// this is a comment')
print(s)  # => 'const foo = "bar";\n'

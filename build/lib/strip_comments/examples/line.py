import strip_comments.strip as strip

s = strip.line('const foo = "bar";// this is a comment\n /* me too */')
print(s)  # 'const foo = "bar";\n /* me too */'

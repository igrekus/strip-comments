import re

ESCAPED_CHAR_REGEX = re.compile(r'^\\.')
QUOTED_STRING_REGEX = re.compile(r'^([\'"`])((?:\\\1|[^\1])+?)(\1)')
NEWLINE_REGEX = re.compile(r'^\r*\n')


ada = {
    'LINE_REGEX': re.compile(r'^--.*'),
}

apl = {
    'LINE_REGEX': re.compile('^⍝.*'),
}

applescript = {
  'BLOCK_OPEN_REGEX': re.compile(r'^\(\*'),
  'BLOCK_CLOSE_REGEX': re.compile(r'^\*\)'),
}

haskell = {
  'BLOCK_OPEN_REGEX': re.compile(r'^\{-'),
  'BLOCK_CLOSE_REGEX': re.compile(r'^-}'),
  'LINE_REGEX': re.compile(r'^--.*'),
}

html = {
  'BLOCK_OPEN_REGEX': re.compile(r'^\n*<!--(?!-?>)'),
  'BLOCK_CLOSE_REGEX': re.compile(r'^(?<!(?:<!-))-->'),
  'BLOCK_CLOSE_LOOSE_REGEX': re.compile(r'^(?<!(?:<!-))--\s*>'),
  'BLOCK_CLOSE_STRICT_NEWLINE_REGEX': re.compile(r'^(?<!(?:<!-))-->(\s*\n+|\n*)'),
  'BLOCK_CLOSE_STRICT_LOOSE_REGEX': re.compile(r'^(?<!(?:<!-))--\s*>(\s*\n+|\n*)'),
}

javascript = {
  'BLOCK_OPEN_REGEX': re.compile(r'^/\*\*?(!?)'),
  'BLOCK_CLOSE_REGEX': re.compile(r'^\*/(\n?)'),
  'LINE_REGEX': re.compile(r'^//(!?).*'),
}

lua = {
  'BLOCK_OPEN_REGEX': re.compile(r'^--\[\['),
  'BLOCK_CLOSE_REGEX': re.compile(r'^]]'),
  'LINE_REGEX': re.compile(r'^--.*'),
}

matlab = {
  'BLOCK_OPEN_REGEX': re.compile(r'^%{'),
  'BLOCK_CLOSE_REGEX': re.compile(r'^%}'),
  'LINE_REGEX': re.compile(r'^%.*'),
}

perl = {
  'LINE_REGEX': re.compile(r'^#.*'),
}

php = {
  **javascript,
  'LINE_REGEX': re.compile(r'^(#|//).*?(?=\?>|\n)'),
}

python = {
  'BLOCK_OPEN_REGEX': re.compile(r'^"""'),
  'BLOCK_CLOSE_REGEX': re.compile(r'^"""'),
  'LINE_REGEX': re.compile(r'^#.*'),
}

ruby = {
  'BLOCK_OPEN_REGEX': re.compile(r'^=begin'),
  'BLOCK_CLOSE_REGEX': re.compile(r'^=end'),
  'LINE_REGEX': re.compile(r'^#.*'),
}

shebang = hashbang = {
  'LINE_REGEX': re.compile(r'^#!.*'),
}

c = javascript
csharp = javascript
css = javascript
java = javascript
js = javascript
less = javascript
pascal = applescript
ocaml = applescript
sass = javascript
sql = ada
swift = javascript
ts = javascript
typescript = javascript
xml = html

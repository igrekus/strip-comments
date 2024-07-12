import re

ESCAPED_CHAR_RE = re.compile(r'^\\.')
QUOTED_STRING_RE = re.compile(r'^([\'"`])((?:\\\1|[^\1])+?)(\1)')
NEWLINE_RE = re.compile(r'^\r*\n')
LETTER_RE = re.compile(r'\w$')
TEXT_RE = re.compile(r'^[a-zABD-Z0-9\t ]+')


ada = {
    'LINE_RE': re.compile(r'^--.*'),
}

apl = {
    'LINE_RE': re.compile('^⍝.*'),
}

applescript = {
  'BLOCK_OPEN_RE': re.compile(r'^\(\*'),
  'BLOCK_CLOSE_RE': re.compile(r'^\*\)'),
}

haskell = {
  'BLOCK_OPEN_RE': re.compile(r'^\{-'),
  'BLOCK_CLOSE_RE': re.compile(r'^-}'),
  'LINE_RE': re.compile(r'^--.*'),
}

html = {
  'BLOCK_OPEN_RE': re.compile(r'^\n*<!--(?!-?>)'),
  'BLOCK_CLOSE_RE': re.compile(r'^(?<!(?:<!-))-->'),
  'BLOCK_CLOSE_LOOSE_RE': re.compile(r'^(?<!(?:<!-))--\s*>'),
  'BLOCK_CLOSE_STRICT_NEWLINE_RE': re.compile(r'^(?<!(?:<!-))-->(\s*\n+|\n*)'),
  'BLOCK_CLOSE_STRICT_LOOSE_RE': re.compile(r'^(?<!(?:<!-))--\s*>(\s*\n+|\n*)'),
}

javascript = {
  'BLOCK_OPEN_RE': re.compile(r'^/\*\*?(!?)'),
  'BLOCK_CLOSE_RE': re.compile(r'^\*/(\n?)'),
  'LINE_RE': re.compile(r'^//(!?).*'),
}

lua = {
  'BLOCK_OPEN_RE': re.compile(r'^--\[\['),
  'BLOCK_CLOSE_RE': re.compile(r'^]]'),
  'LINE_RE': re.compile(r'^--.*'),
}

matlab = {
  'BLOCK_OPEN_RE': re.compile(r'^%{'),
  'BLOCK_CLOSE_RE': re.compile(r'^%}'),
  'LINE_RE': re.compile(r'^%.*'),
}

perl = {
  'LINE_RE': re.compile(r'^#.*'),
}

php = {
  **javascript,
  'LINE_RE': re.compile(r'^(#|//).*?(?=\?>|\n)'),
}

python = {
  'BLOCK_OPEN_RE': re.compile(r'^"""'),
  'BLOCK_CLOSE_RE': re.compile(r'^"""'),
  'LINE_RE': re.compile(r'^#.*'),
}

ruby = {
  'BLOCK_OPEN_RE': re.compile(r'^=begin'),
  'BLOCK_CLOSE_RE': re.compile(r'^=end'),
  'LINE_RE': re.compile(r'^#.*'),
}

shebang = hashbang = {
  'LINE_RE': re.compile(r'^#!.*'),
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

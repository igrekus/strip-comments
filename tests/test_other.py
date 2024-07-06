import pathlib

import pytest

import strip


fixt = pathlib.Path('/home/ipx/source/python/strip-comments/tests/fixtures/other')
exp = pathlib.Path('/home/ipx/source/python/strip-comments/tests/expected/other')


def test_strips_ada():
    source = (fixt / 'ada.txt').read_text()
    expected = (exp / 'ada.txt').read_text()

    assert strip.strip(source, language='ada', preserve_newlines=True) == expected


def test_strips_apl():
    source = (fixt / 'apl.txt').read_text()
    expected = (exp / 'apl.txt').read_text()

    assert strip.strip(source, language='apl', preserve_newlines=True) == expected


def test_strips_c():
    source = (fixt / 'c.txt').read_text()
    expected = (exp / 'c.txt').read_text()

    assert strip.strip(source, language='c', preserve_newlines=True) == expected


def test_strips_apple_script():
    source = (fixt / 'applescript.txt').read_text()
    expected = (exp / 'applescript.txt').read_text()

    assert strip.strip(source, language='applescript') == expected


def test_strips_haskell():
    source = '''{- this is a comment
on more lines -}
-- and this is a comment on one line
putStrLn "Wikipedia"  -- this is another comment
'''
    expected = '\n\nputStrLn "Wikipedia"  \n'

    assert strip.strip(source, language='haskell') == expected


def test_strips_lua():
    source = (fixt / 'lua.txt').read_text()
    expected = (exp / 'lua.txt').read_text()

    assert strip.strip(source, language='lua') == expected


def test_strips_matlab():
    source = (fixt / 'matlab.txt').read_text()
    expected = (exp / 'matlab.txt').read_text()

    assert strip.strip(source, language='matlab') == expected


def test_strips_ocaml():
    source = (fixt / 'ocaml.txt').read_text()
    expected = (exp / 'ocaml.txt').read_text()

    assert strip.strip(source, language='ocaml') == expected


def test_strips_pascal():
    source = (fixt / 'pascal.txt').read_text()
    expected = (exp / 'pascal.txt').read_text()

    assert strip.strip(source, language='pascal') == expected


def test_strips_php():
    source = (fixt / 'php.txt').read_text()
    expected = (exp / 'php.txt').read_text()

    assert strip.strip(source, language='php') == expected


def test_strips_perl():
    source = (fixt / 'perl.txt').read_text()
    expected = (exp / 'perl.txt').read_text()

    assert strip.strip(source, language='perl') == expected


def test_strips_python():
    source = (fixt / 'python.txt').read_text()
    expected = (exp / 'python.txt').read_text()

    assert strip.strip(source, language='python') == expected


def test_strips_ruby():
    source = (fixt / 'ruby.txt').read_text()
    expected = (exp / 'ruby.txt').read_text()

    assert strip.strip(source, language='ruby') == expected


def test_strips_shebang():
    source = (fixt / 'shebang.txt').read_text()
    expected = (exp / 'shebang.txt').read_text()

    assert strip.strip(source, language='shebang') == expected


def test_strips_sql():
    source = (fixt / 'sql.txt').read_text()
    expected = (exp / 'sql.txt').read_text()

    assert strip.strip(source, language='sql') == expected


def test_strips_swift():
    source = (fixt / 'swift.txt').read_text()
    expected = (exp / 'swift.txt').read_text()

    assert strip.strip(source, language='swift') == expected

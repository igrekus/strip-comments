import pathlib

import strip


def test_strip_generic():
    sample = 'No <!-- I should be gone-->comment'
    actual = strip.strip(sample, language='html')

    assert actual == 'No comment'


def test_not_strip_inside_quotes():
    sample = 'No "<!-- I should NOT be gone-->"comment'
    actual = strip.strip(sample, language='html')

    assert actual == sample


def test_not_strip_comment_parts_inside_quotes():
    name = 'quoted'
    sample = pathlib.Path(f'/home/ipx/source/python/strip-comments/tests/fixtures/html/{name}.html').read_text()
    expected = pathlib.Path(f'/home/ipx/source/python/strip-comments/tests/expected/html/{name}.html').read_text()
    actual = strip.strip(sample, language='html')

    assert actual == expected


def test_strip_multiline():
    name = 'multiline'
    sample = pathlib.Path(f'/home/ipx/source/python/strip-comments/tests/fixtures/html/{name}.html').read_text()
    expected = pathlib.Path(f'/home/ipx/source/python/strip-comments/tests/expected/html/{name}.html').read_text()
    actual = strip.strip(sample, language='html')

    assert actual == expected


def test_strip_comments_with_only_dashes():
    name = 'dashes'
    sample = pathlib.Path(f'/home/ipx/source/python/strip-comments/tests/fixtures/html/{name}.html').read_text()
    expected = pathlib.Path(f'/home/ipx/source/python/strip-comments/tests/expected/html/{name}.html').read_text()
    actual = strip.strip(sample, language='html')

    assert actual == expected

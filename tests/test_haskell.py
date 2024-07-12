from strip_comments import strip

source = '''{- this is a comment
on more lines -}
-- and this is a comment on one line
putStrLn "Wikipedia"  -- this is another comment
'''

expected = '\n\nputStrLn "Wikipedia"  \n'


def test_strips_haskell():

    assert strip.strip(source, language='haskell') == expected

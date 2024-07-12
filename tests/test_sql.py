from strip_comments import strip

source = '''SQL
Comments in SQL are in single-line-only form, when using two dashes:

-- This is a single line comment
-- followed by a second line
SELECT COUNT(*)
       FROM Authors
       WHERE Authors.name = 'Smith'; -- Note: we only want 'smith'
                                     -- this comment appears after SQL code
'''

expected = '''SQL
Comments in SQL are in single-line-only form, when using two dashes:



SELECT COUNT(*)
       FROM Authors
       WHERE Authors.name = 'Smith'; 
                                     
'''


def test_strips_sql():

    assert strip.strip(source, language='sql') == expected

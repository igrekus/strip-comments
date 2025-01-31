from strip_comments import strip

source = '''(* test diagonals *)
columnDifference := testColumn - column;
if (row + columnDifference = testRow) or
    .......
'''

expected = '''
columnDifference := testColumn - column;
if (row + columnDifference = testRow) or
    .......
'''


def test_strips_pascal():

    assert strip.strip(source, language='pascal') == expected

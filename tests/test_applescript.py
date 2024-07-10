import strip_comments.strip as strip

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


def test_strips_applescript():

    assert strip.strip(source, language='applescript') == expected

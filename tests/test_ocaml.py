import strip


source = '''OCaml
OCaml uses nestable comments, which is useful when commenting a code block.

codeLine(* comment level 1(*comment level 2*)*)
'''

expected = '''OCaml
OCaml uses nestable comments, which is useful when commenting a code block.

codeLine
'''


def test_strips_ocaml():

    assert strip.strip(source, language='ocaml') == expected

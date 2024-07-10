import strip_comments.strip as strip

source = '''Lua
The Lua programming language uses double-hyphens, `--`, for single line comments in a similar way to Ada, Eiffel, Haskell, SQL and VHDL languages. Lua also has block comments, which start with `--[[` and run until a closing `]]`

For example:

--[[A multi-line
long comment
]]
print(20)   -- print the result
A common technique to comment out a piece of code,[44] is to enclose the code between `--[[` and `--]]`, as below:

--[[
print(10)
--]]
-- no action (commented out)
In this case, it's possible to reactivate the code by adding a single hyphen to the first line:

---[[
print(10)
--]]
--> 10
In the first example, the `--[[` in the first line starts a long comment, and the two hyphens in the last line are still inside that comment. In the second example, the sequence `---[[` starts an ordinary, single-line comment, so that the first and the last lines become independent comments. In this case, the print is outside comments. In this case, the last line becomes an independent comment, as it starts with `--`.

Long comments in Lua can be more complex than these, as you can read in the section called "Long strings" c.f. Programming in Lua.
'''

expected = '''Lua
The Lua programming language uses double-hyphens, `--`, for single line comments in a similar way to Ada, Eiffel, Haskell, SQL and VHDL languages. Lua also has block comments, which start with `--[[` and run until a closing `]]`

For example:


print(20)   
A common technique to comment out a piece of code,[44] is to enclose the code between `--[[` and `--]]`, as below:



In this case, it's possible to reactivate the code by adding a single hyphen to the first line:


print(10)


In the first example, the `--[[` in the first line starts a long comment, and the two hyphens in the last line are still inside that comment. In the second example, the sequence `---[[` starts an ordinary, single-line comment, so that the first and the last lines become independent comments. In this case, the print is outside comments. In this case, the last line becomes an independent comment, as it starts with `--`.

Long comments in Lua can be more complex than these, as you can read in the section called "Long strings" c.f. Programming in Lua.
'''


def test_strips_lua():

    assert strip.strip(source, language='lua') == expected

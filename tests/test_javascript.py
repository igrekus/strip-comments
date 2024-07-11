import json
import pathlib
import time

import pytest

import strip_comments.strip as strip


def test_strips_all_generic():
    assert strip.strip("'foo'; // this is a comment\n/* me too */ var abc = 'xyz';") == '\'foo\'; \n var abc = \'xyz\';'


def test_strips_unclosed_invalid_blocks():
    assert strip.strip("'foo'; /* I am invalid ") == '\'foo\'; '


def test_strips_line():
    assert strip.line('foo // this is a comment\n/* me too */') == 'foo \n/* me too */'


def test_not_strips_escaped_slashes():
    assert strip.line("'foo/bar'.replace(/o\\//, 'g')") == "'foo/bar'.replace(/o\\//, 'g')"


def test_strips_blocks():
    assert strip.block('foo // this is a comment\n/* me too */') == 'foo // this is a comment\n'


def test_strips_first_not_strips_rest():
    source = '''/*!
 * update-banner <https://github.com/jonschlinkert/update-banner>
 *
 * Copyright (c) 2015, Jon Schlinkert.
 * Licensed under the MIT License.
 */

'use strict';

/**
 * Another comment
 */

function someFunction() {
  // body...
}'''

    expected = '''
'use strict';

/**
 * Another comment
 */

function someFunction() {
  // body...
}'''

    assert strip.first(source) == expected


def test_strips_first_if_not_protected():
    source = '''/*!
 * update-banner <https://github.com/jonschlinkert/update-banner>
 *
 * Copyright (c) 2015, Jon Schlinkert.
 * Licensed under the MIT License.
 */

'use strict';

/**
 * Another comment
 */

function someFunction() {
  // body...
}'''

    expected = '''/*!
 * update-banner <https://github.com/jonschlinkert/update-banner>
 *
 * Copyright (c) 2015, Jon Schlinkert.
 * Licensed under the MIT License.
 */

'use strict';


function someFunction() {
  // body...
}'''

    assert strip.first(source, keep_protected=True) == expected


def test_not_strips_non_comments_in_quotes():
    source = '''window.amino_cec_callback = function (tag, source, destination, body) {
    debug("///////////// cec_callback ////////////////////");
    debug(tag + " " + source + " " + destination + " " + body);
    debug("///////////// cec_callback ////////////////////");
};

const foo = {
  "config": {
    "properties": {
      "device_id": {
        "type": "string",
        "title": "Device ID",
        "label": {
          "$ref": "/rpcs/device_ids#thermostats/*/{name}"
        },
        "oneOf": [{
          "$ref": "/rpcs/device_ids#thermostats/*/{device_id}"
        }]
      }
    },
    "required": ["device_id"],
    "disposition": ["device_id"]
  }
};'''

    expected = source

    assert strip.strip(source) == expected


def test_no_infinite_loop_on_unclosed_comments():
    # globs basically
    source = 'if (accept == \'video/*\') {'
    expected = source

    assert strip.strip(source) == expected


def test_not_mangles_json():
    source = '''{
  "name": "strip-comments",
  "description": "Strip line and/or block comments from a string. Blazing fast, and works with JavaScript, Sass, CSS, Less.js, and a number of other languages.",
  "version": "2.0.1",
  "homepage": "https://github.com/jonschlinkert/strip-comments",
  "author": "Jon Schlinkert (https://github.com/jonschlinkert)",
  "repository": "jonschlinkert/strip-comments",
  "bugs": {
    "url": "https://github.com/jonschlinkert/strip-comments/issues"
  },
  "license": "MIT",
  "files": [
    "index.js",
    "lib"
  ],
  "main": "index.js",
  "engines": {
    "node": ">=10"
  },
  "scripts": {
    "test": "mocha",
    "cover": "nyc --reporter=text --reporter=html mocha"
  },
  "devDependencies": {
    "gulp-format-md": "^2.0.0",
    "mocha": "^6.2.2",
    "nyc": "^14.1.1"
  },
  "keywords": [
    "ada comments",
    "apl comments",
    "applescript comments",
    "block comment",
    "block",
    "block-comment",
    "c comments",
    "code comment",
    "comment",
    "comments",
    "csharp comments",
    "css comments",
    "css",
    "hashbang comments",
    "haskell comments",
    "html comments",
    "java comments",
    "javascript comments",
    "javascript",
    "js",
    "less comments",
    "less css",
    "less",
    "less.js",
    "lessjs",
    "line comment",
    "line comments",
    "line",
    "line-comment",
    "line-comments",
    "lua comments",
    "matlab comments",
    "ocaml comments",
    "pascal comments",
    "perl comments",
    "php comments",
    "python comments",
    "remove",
    "ruby comments",
    "sass comments",
    "sass",
    "shebang comments",
    "sql comments",
    "strip",
    "swift comments",
    "typscript comments",
    "xml comments"
  ],
  "verb": {
    "toc": true,
    "layout": "default",
    "tasks": [
      "readme"
    ],
    "plugins": [
      "gulp-format-md"
    ],
    "helpers": [
      "./examples/support/helpers.js"
    ],
    "related": {
      "list": [
        "code-context",
        "extract-comments",
        "parse-code-context",
        "parse-comments"
      ]
    },
    "lint": {
      "reflinks": true
    }
  }
}'''
    before = json.loads(source)

    res = strip.strip(source)
    after = json.loads(res)

    assert before == after


def test_strips_all_but_not_slash_star_slash():
    # also globs
    source = "/* I will be stripped */\nvar path = '/this/should/*/not/be/stripped';"
    actual = strip.strip(source)
    expected = "var path = '/this/should/*/not/be/stripped';";

    assert actual == expected


def test_strips_all_but_not_globstars():
    source = "var path = './do/not/strip/globs/**/*.js';"
    actual = strip.strip(source)

    assert actual == "var path = './do/not/strip/globs/**/*.js';"


def test_strips_all_but_not_globstars_and_protected():
    source = 'var partPath = \'./path/*/to/scripts/**/\'; //! line comment'
    actual = strip.strip(source, safe=True)

    assert actual == 'var partPath = \'./path/*/to/scripts/**/\'; //! line comment'


def test_strips_all_but_not_any_globs():
    # TODO add original comment
    source = 'var partPath = \'./path/*/*something/test.txt\';'
    actual = strip.strip(source)

    assert actual == 'var partPath = \'./path/*/*something/test.txt\';'


def test_strips_all_but_not_any_globs_2():
    # TODO add original comment
    source = 'var partPath = \'./path/*/*something/*.js\';'
    actual = strip.strip(source)

    assert actual == "var partPath = './path/*/*something/*.js';"


def test_not_touches_code_with_no_comments():
    source = ''''use strict';

process.stdout.write('string literals: ');
console.dir({
  str0: '&apos;',
  str1: "&quot;",
  str2: ". // ' \\ . // ' \\ .",
});

process.stdout.write('RegExp literals: ');
console.dir({
  regexp0: /I'm the easiest in Chomsky hierarchy!/,
});
'''

    expected = source

    assert strip.strip(source) == expected


def test_works_with_comments_which_are_substrings_of_a_later_comment():
    source = (
        '// this is a substring\n'
        '// this is a substring of a larger comment\n'
        'someCode();\n'
        'someMoreCode();\n'
    )
    actual = strip.strip(source)
    expected = (
        '\n'
        '\n'
        'someCode();\n'
        'someMoreCode();\n'
    )
    assert actual == expected


# error handling
def test_raises_value_error_when_strip_arg_is_not_str():
    with pytest.raises(ValueError) as ex:
        strip.strip(123)

    assert ex.value.args[0] == 'Expected input to be a string'


def test_raises_value_error_when_block_arg_is_not_str():
    with pytest.raises(ValueError) as ex:
        strip.block(123)

    assert ex.value.args[0] == 'Expected input to be a string'


def test_raises_value_error_when_line_arg_is_not_str():
    with pytest.raises(ValueError) as ex:
        strip.line(123)

    assert ex.value.args[0] == 'Expected input to be a string'


def test_not_raises_on_empty_str_returns_empty_str():
    actual = strip.strip('')
    expected = ''

    assert isinstance(actual, str)
    assert actual == expected


# strip all or empty
def test_strips_all_file():
    source = '''/*!
 * strip this multiline
 * block comment
 */
'use strict';

/**!
 * and this multiline
 * block comment
 */
var foo = function(/* and these single-line block comment */) {};

/**
 * and this
 * multiline block
 * comment
 */
var bar = function(/* and that */) {};

var baz = '//bar baz not a comment';

// this single-line line comment
var qux = function() {
  // this multiline
  // line comment
  var some = true;
  //this
  var fafa = true; //and this
  // var also = 'that';
  var but = 'not'; //! that comment
};

// also this multiline
// line comment
var fun = false;
var path = '/path/to/*/something/that/not/be/stripped.js';
var globstar = '/path//to//globstar/not/be/stripped/**/*.js';'''

    expected = ''''use strict';

var foo = function() {};

var bar = function() {};

var baz = '//bar baz not a comment';


var qux = function() {
  
  
  var some = true;
  
  var fafa = true; 
  
  var but = 'not'; 
};



var fun = false;
var path = '/path/to/*/something/that/not/be/stripped.js';
var globstar = '/path//to//globstar/not/be/stripped/**/*.js';'''

    assert strip.strip(source) == expected


def test_not_strips_bang_comments():
    source = '''/*!
 * strip this multiline
 * block comment
 */
'use strict';

/**!
 * and this multiline
 * block comment
 */
var foo = function(/* and these single-line block comment */) {};

/**
 * and this
 * multiline block
 * comment
 */
var bar = function(/* and that */) {};

var baz = '//bar baz not a comment';

// this single-line line comment
var qux = function() {
  // this multiline
  // line comment
  var some = true;
  //this
  var fafa = true; //and this
  // var also = 'that';
  var but = 'not'; //! that comment
};

// also this multiline
// line comment
var fun = false;
var path = '/path/to/*/something/that/not/be/stripped.js';
var globstar = '/path//to//globstar/not/be/stripped/**/*.js';'''

    expected = '''/*!
 * strip this multiline
 * block comment
 */
'use strict';

/**!
 * and this multiline
 * block comment
 */
var foo = function() {};

var bar = function() {};

var baz = '//bar baz not a comment';

// this single-line line comment
var qux = function() {
  // this multiline
  // line comment
  var some = true;
  //this
  var fafa = true; //and this
  // var also = 'that';
  var but = 'not'; //! that comment
};

// also this multiline
// line comment
var fun = false;
var path = '/path/to/*/something/that/not/be/stripped.js';
var globstar = '/path//to//globstar/not/be/stripped/**/*.js';'''

    assert strip.block(source, safe=True) == expected


def test_strips_all_line_but_not_bang_comments():
    source = '''/**
 * this block comment
 * will not be striped
 */

'use strict';

//! and this multiline
//! block comment
var foo = function(/* and these single-line block comment */) {};

/**
 * and this
 * multiline block
 * comment
 */
var bar = function(/* and that */) {};

//will be removed
var baz = function() {
  // this multiline
  // line comment
  var some = true;
  // will be
  var fafa = true;
  // var removed = 'yes';
  var but = 'not'; //! that comment
};

var path = '/path/to/*/something/that/not/be/stripped.js';
var globstar = '/path/to/globstar/not/be/stripped/**/*.js';
'''

    expected = '''/**
 * this block comment
 * will not be striped
 */

'use strict';

//! and this multiline
//! block comment
var foo = function(/* and these single-line block comment */) {};

/**
 * and this
 * multiline block
 * comment
 */
var bar = function(/* and that */) {};


var baz = function() {
  
  
  var some = true;
  
  var fafa = true;
  
  var but = 'not'; //! that comment
};

var path = '/path/to/*/something/that/not/be/stripped.js';
var globstar = '/path/to/globstar/not/be/stripped/**/*.js';
'''

    assert strip.line(source, safe=True) == expected


def test_strips_all_but_keeps_newlines():
    source = '''/*!
 * strip this multiline
 * block comment
 */
'use strict';

/**!
 * and this multiline
 * block comment
 */
var foo = function(/* and these single-line block comment */) {};

/**
 * and this
 * multiline block
 * comment
 */
var bar = function(/* and that */) {};

var baz = '//bar baz not a comment';

// this single-line line comment
var qux = function() {
  // this multiline
  // line comment
  var some = true;
  //this
  var fafa = true; //and this
  // var also = 'that';
  var but = 'not'; //! that comment
};

// also this multiline
// line comment
var fun = false;
var path = '/path/to/*/something/that/not/be/stripped.js';
var globstar = '/path//to//globstar/not/be/stripped/**/*.js';'''

    expected = '''



'use strict';





var foo = function() {};






var bar = function() {};

var baz = '//bar baz not a comment';


var qux = function() {
  
  
  var some = true;
  
  var fafa = true; 
  
  var but = 'not'; 
};



var fun = false;
var path = '/path/to/*/something/that/not/be/stripped.js';
var globstar = '/path//to//globstar/not/be/stripped/**/*.js';'''

    assert strip.strip(source, preserve_newlines=True) == expected


def test_strips_blocks_inside_function():
    actual = strip.block('var bar = function(/* this is a comment*/) {return;};')

    assert actual == 'var bar = function() {return;};'


def test_strips_blocks_before_and_inside_function():
    actual = strip.block('/* this is a comment */\nvar bar = function(/*this is a comment*/) {return;};')

    assert actual == 'var bar = function() {return;};'


def test_strips_blocks_before_inside_and_after_function():
    actual = strip.block('/* this is a comment */var bar = function(/*this is a comment*/) {return;};\n/* this is a comment*/')

    assert actual == 'var bar = function() {return;};\n'


def test_strips_line_generic():
    actual = strip.line('// this is a line comment\nvar bar = function(/*this is a comment*/) {return;};')

    assert actual == '\nvar bar = function(/*this is a comment*/) {return;};'


def test_strips_line_with_leading_whitespace():
    actual = strip.line(' //                           this should be stripped')

    assert actual == ' '


def test_strips_line_in_quoted_strings():
    actual = strip.line('var foo = "//this is not a comment";')

    assert actual == 'var foo = "//this is not a comment";'


def test_strips_line_after_quoted_strings():
    actual = strip.line('var foo = "//this is not a comment"; //this should be stripped')

    assert actual == 'var foo = "//this is not a comment"; '


def test_strips_and_not_whitespace_sensitive():
    actual = strip.line('var foo = "//this is not a comment"; //                           this should be stripped')

    assert actual == 'var foo = "//this is not a comment"; '


def test_not_strips_urls_in_quoted_strings():
    actual = strip.line('var foo = "http://github.com"; //                           this should be stripped')

    assert actual == 'var foo = "http://github.com"; '


def test_strips_urls_in_line_comment():
    actual = strip.line('// http://github.com"')

    assert actual == ''


def test_strips_urls_in_blocks():
    actual = strip.block('/**\n* http://github.com\n *\n */')

    assert actual == ''


def test_should_strip_line_before_function_but_not_blocks():
    actual = strip.line('/* this is a comment */\n//this is a comment\nvar bar = function(/*this is a comment*/) {return;};')

    assert actual == '/* this is a comment */\n\nvar bar = function(/*this is a comment*/) {return;};'


def test_should_strip_line_before_and_after_function_but_not_blocks():
    actual = strip.line('/* this is a comment */\n//this is a comment\nvar bar = function(/*this is a comment*/) {return;};\n//this is a line comment')

    assert actual == '/* this is a comment */\n\nvar bar = function(/*this is a comment*/) {return;};\n'


def test_should_not_timeout():
    time_start = time.monotonic_ns()
    actual = strip.strip('''
        console.log(tpl\`
        123
      \`);
      ${Array(10).fill('console.log(/^http:\\/\\//.test("1"));').join('\n')}\n
      ${Array(100).fill('console.log("1");').join('\n')}\n'''
    )
    expected = actual
    time_end = time.monotonic_ns()

    assert actual == expected
    assert time_end - time_start < 500_000_000  # 500 ms

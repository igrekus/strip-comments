# strip-comments
[![build](https://github.com/igrekus/strip-comments/actions/workflows/python-package.yml/badge.svg)](https://github.com/igrekus/strip-comments/actions/workflows/python-package.yml)

Strip line and/or block comments from a string. Works with JavaScript, Sass, CSS, Less.js, and a number of other languages.

This repo is a port of [strip-comments](https://github.com/jonschlinkert/strip-comments)

- [What is it?](#what-is-it)
- [Install](#install)
- [CLI usage](#cli-usage)
- [Python API](#python-api)
- [About](#about)
- [TODO](#todo)

## What is it?

The utility receives a file as input and prints its content with comments removed. Handles line comments and/or block comments. Optionally removes the first comment only or ignores protected comments.

Supports:

* ada
* apl
* applescript
* c
* csharp
* css
* hashbang
* haskell
* html
* java
* javascript
* less
* lua
* matlab
* ocaml
* pascal
* perl
* php
* python
* ruby
* sass
* shebang
* sql
* swift
* typscript
* xml

## Install

Via pypi (pypi package TBD)
```sh
pip install strip-comments
```

From source
```sh
git clone https://github.com/igrekus/strip-comments.git
cd strip-comments
pip install .
```

## CLI usage

By default all comments are stripped.

```bash
cat sample-file.js
```
```text
'use strict';
/* -------------------------
   This is the comment body.
*/ -------------------------
const foo = 'bar'; // another line 
```
```bash
$ strip-comments sample-file.js
```
```text
'use strict';



const foo = 'bar'; 
```

For more use cases see the command help.

## Python API

### strip.strip()

Remove all code comments from the given `source`, including protected comments that start with `!`, unless `keep_protected` is passed true.

**Args**

- `source`: **str** -- input Python string to strip comments from
- `block`: **bool** -- remove block comments
- `line`: **bool** -- remove line comments
- `first`: **bool** -- remove only the first comment
- `language`: **str** -- programming language the string is written in
- `keep_protected`: **bool** -- keep the protected comments (starting with a `!` as the first char) 
- `preserve_newlines`: **bool** -- preserve newlines after comments are removed
* `returns`: **str** -- modified source string

**Example**

```python
from strip_comments import strip

print(strip.strip('const foo = "bar";// this is a comment\n /* me too */'))
# >>> const foo = "bar";
```

### strip.block()

Convenience wrapper, remove block comments only.

**Example**

```python
from strip_comments import strip

print(strip.block('const foo = "bar";// this is a comment\n /* me too */'))
# >>> const foo = "bar";// this is a comment
```

### strip.line()

Convenience wrapper, remove line comments only.

**Example**

```python
from strip_comments import strip

print(strip.line('const foo = "bar";// this is a comment\n /* me too */'))
# >>> const foo = "bar";\n/* me too */
```

### strip.first()

Convenience wrapper, remove only the first comment from the given `source`. If `keep_protected` is passed `True`, the first non-protected comment will be removed.

**Example**

```python
from strip_comments import strip

print(strip.first('const foo = "bar"; //! protected\n // removed', keep_protected=True))
# >>> const foo = "bar"; //! protected\n
```

## About

<details>
<summary><strong>Contributing</strong></summary>

Pull requests and stars are always welcome. For bugs and feature requests, please [create](https://github.com/igrekus/strip-comments/issues) an issue.
</details>

<details>
<summary><strong>Running Tests</strong></summary>

```sh
pip install pytest
pytest tests
```
</details>

### License

Copyright © 2024-present, [igrekus](https://github.com/igrekus).
Released under the [MIT License](LICENSE).

## TODO

- [x] port code
- [x] make code pythonic (kinda)
- [x] add CLI entrypoint
- [x] update readme
- [x] add the ability to handle directories on the input
- [ ] make a pypi package
- [ ] expand other-lang tests
- [ ] add header [banner](https://github.com/jonschlinkert/update-banner)?
- [ ] add fancy badges to readme

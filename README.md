# Flake8 - check for blank lines before statements

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-proprietary-blue)
![Coverage](https://img.shields.io/badge/Coverage-92%25-brightgreen?logo=pytest&logoColor=white)
![CI](https://github.com/ts-mk/flake8-bbs/actions/workflows/tests.yml/badge.svg)

## Introduction

While PEP8 doesn't provide any opinion on the use of blank lines before statements, some people believe that adding them improves code readability which is otherwise hindered despite syntax highlighting that modern code editors provide, as demonstrated in the following example:

```python
import os

a = 3
if a == 1:
    print(a)
with os.open('filename') as f:
    content = f.read_lines()
if a == 2:
    print(a)
```

The plugin therefore checks for a blank line before each statement as long as it's **not a first line of code within a module** and **not a first statement within another statement**.

## List of statements and their error codes

* `assert`: BBS001
* `async for`: BBS002
* `async def`: BBS003
* `async with`: BBS004
* `break`: BBS005
* `class`: BBS006
* `continue`: BBS007
* `del`: BBS008
* `for`: BBS009
* `def`: BBS010
* `global`: BBS011
* `if`: BBS012
* `import`: BBS013
* `import from`: BBS014
* `nonlocal`: BBS015
* `pass`: BBS016
* `raise`: BBS017
* `return`: BBS018
* `try`: BBS019
* `while`: BBS020
* `with`: BBS021
* `yield`: BBS022
* `yield from`: BBS023

## Exclusion of errors

The plugin checks for a blank line before each statement. This however is not completely practical (e.g. multiple `import` statements following each other are pretty standard), nevermind that the same/conflicting checks might already be applied by another plugin (e.g. checks by [flake8-import-order]()) or should be handled by some other formatting tools (e.g. [black](https://github.com/psf/black)). Therefore, you most probably want to exclude some checks using Flake8's `ignore` option.

### Recommended exclusions

```ini
[flake8]
ignore = BBS001, BBS003, BBS005, BBS006, BBS007, BBS008, BBS010, BBS013, BBS014, BBS016
```

### All but compound statements

Keeps only some [compound statements](https://docs.python.org/3.9/reference/compound_stmts.html) enabled:

```ini
[flake8]
ignore = BBS001, BBS003, BBS004, BBS005, BBS006, BBS007, BBS008, BBS010, BBS011, BBS013, BBS014, BBS015, BBS016, BBS017, BBS018, BBS022, BBS023
```

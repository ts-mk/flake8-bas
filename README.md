# Flake8 - check for blank lines before statements

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-proprietary-blue)
![Coverage](https://img.shields.io/badge/Coverage-96%25-brightgreen?logo=pytest&logoColor=white)
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

The plugin therefore checks for a blank line before each statement as long as it's **not the first line of code within a module** and **not the first statement within another statement**.


## Requirements

* Python >= 3.8
* flake8 >= 4.0.0


## Plugin state

Until version 1.0.0 is reached, this plugin is considered as **not ready for production**.


## Statements and their error codes

| Statement     | Code   |
|---------------|--------|
| `assert`      | BBS010 |
| `async for`   | BBS020 |
| `async def`   | BBS030 |
| `async with`  | BBS040 |
| `break`       | BBS050 |
| `class`       | BBS060 |
| `continue`    | BBS070 |
| `del`         | BBS080 |
| `for`         | BBS090 |
| `def`         | BBS100 |
| `global`      | BBS110 |
| `if`          | BBS120 |
| `import`      | BBS130 |
| `import from` | BBS140 |
| `nonlocal`    | BBS150 |
| `pass`        | BBS160 |
| `raise`       | BBS170 |
| `return`      | BBS180 |
| `try`         | BBS190 |
| `while`       | BBS200 |
| `with`        | BBS210 |
| `yield`       | BBS220 |
| `yield from`  | BBS230 |


## Exclusion of errors

The plugin checks for a blank line before **every** statement. This however is not completely practical (e.g. multiple `import` or `assert` statements following each other are pretty standard), nevermind that the same/conflicting checks might already be applied by another plugin (e.g. checks by [flake8-import-order](https://github.com/PyCQA/flake8-import-order)) or should be handled by other formatting tools (e.g. [black](https://github.com/psf/black)). Therefore, you most probably want to exclude some checks using Flake8's `ignore` option.

### Recommended exclusions

```ini
[flake8]
ignore = BBS010, BBS030, BBS050, BBS060, BBS070, BBS080, BBS100, BBS130, BBS140, BBS160
```

### All but compound statements

Keeps only some [compound statements](https://docs.python.org/3.9/reference/compound_stmts.html) enabled:

```ini
[flake8]
ignore = BBS010, BBS030, BBS040, BBS050, BBS060, BBS070, BBS080, BBS100, BBS110, BBS130, BBS140, BBS150, BBS160, BBS170, BBS180, BBS220, BBS230
```


## Todo

* Compatibility with Python 3.7.
* Config option to allow multiple consecutive statements for the same type of statement, e.g. `assert`, `del`, `import`

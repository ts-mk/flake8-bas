# Flake8 - check for blank lines around statements

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![PyPI](https://img.shields.io/pypi/v/flake8-bas.svg?label=PyPI&logo=PyPI&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?logo=opensourceinitiative&logoColor=white)
![codecov](https://codecov.io/gh/ts-mk/flake8-bas/branch/master/graph/badge.svg?token=PI2I083V09)
![CI](https://github.com/ts-mk/flake8-bas/actions/workflows/tests.yml/badge.svg)

[PEP 8](https://peps.python.org/pep-0008/) recommends to use blank lines only to separate logical sections:

> Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between
> a bunch of related one-liners (e.g. a set of dummy implementations).
>
> Use blank lines in functions, sparingly, to indicate logical sections.

However, adding blank lines before and after compound statements (e.g. `if/else` block) as well as some simple
statements (e.g. `return`) might improve code readability which is otherwise hindered despite syntax highlighting
that modern code editors provide, as demonstrated in the following example:

```python
if 1 == 1:
    print(1)
for n in [2, 3]:
    print(n)
else:
    print(4)
```

...where it might not be immediately apparent that this is not one `if/else` statement but an `if` statement followed by
a `for/else` statement.

This Flake8 plugin therefore checks for a blank line before/after each statement as long as it's **not the first/last
line of code within a module** and **not the first/last statement within a compound statement**.


## Requirements

* Python >= 3.8.1
* Flake8 >= 3.8.0


## Installation

### Pip

```bash
pip install flake8-bas
```

### Poetry

```bash
poetry add flake8-bas
```


## Statements and their error codes

The statements are split into different categories based on whether they are
[simple statements](https://docs.python.org/3.11/reference/simple_stmts.html) or
[compound statements](https://docs.python.org/3.11/reference/compound_stmts.html), and whether the error occurs between
two statements of the same type or not. This allows you to filter entire groups using `BAS` and the first digit,
e.g. `BAS2`.

**Error types:**

* *Before Error* - missing line before a statement as long as the preceding element is not a statement of the same type.
* *After Error* - missing line after a statement as long as the element that follows is not a statement of the same
                  type.
* *Sibling Error* - missing line between two or more consecutive statements of the same type.

### BAS1xx/BAS2xx/BAS3xx: Simple statements

Simple statements, excluding
[expressions](https://docs.python.org/3.11/reference/simple_stmts.html#expression-statements) and
[assignments](https://docs.python.org/3.11/reference/simple_stmts.html#assignment-statements), which are technically
statements as well.

| Statement         | Before Error | After Error | Sibling Error |
|:------------------|:-------------|:------------|:--------------|
| `assert`          | BAS101       | BAS201      | BAS301        |
| `break`           | BAS102       | BAS202      | BAS302        |
| `continue`        | BAS103       | BAS203      | BAS303        |
| `del`             | BAS104       | BAS204      | BAS304        |
| `global`          | BAS105       | BAS205      | BAS305        |
| `import`          | BAS106       | BAS206      | BAS306        |
| `from import`     | BAS107       | BAS207      | BAS307        |
| `nonlocal`        | BAS108       | BAS208      | BAS308        |
| `pass`            | BAS109       | BAS209      | BAS309        |
| `raise`           | BAS110       | BAS210      | BAS310        |
| `return`          | BAS111       | BAS211      | BAS311        |
| `yield`           | BAS112       | BAS212      | BAS312        |
| `yield from`      | BAS113       | BAS213      | BAS313        |

**Note:** Some of these errors shouldn't occur (e.g. `return` followed by another `return`) because having
consecutive siblings of those types does not make sense, but the plugin would raise these errors anyway.

### BAS5xx/BAS6xx/BAS7xx: Compound statements

| Statement    | Before Error | After Error | Sibling Error |
|:-------------|:-------------|:------------|:--------------|
| `class`      | BAS501       | BAS601      | BAS701        |
| `def`        | BAS502       | BAS602      | BAS702        |
| `async def`  | BAS503       | BAS603      | BAS703        |
| `for`        | BAS504       | BAS604      | BAS704        |
| `async for`  | BAS505       | BAS605      | BAS705        |
| `if`         | BAS506       | BAS606      | BAS706        |
| `match`      | BAS507       | BAS607      | BAS707        |
| `try`        | BAS508       | BAS608      | BAS708        |
| `while`      | BAS509       | BAS609      | BAS709        |
| `with`       | BAS510       | BAS610      | BAS710        |
| `async with` | BAS511       | BAS611      | BAS711        |


## Overlapping errors

The extension produces overlapping errors, that is **two statements of different types** following each other would
produce one "before" error and one "after" error pointing to the same line of code:

```python
a = 1

global a
del a
```

This would result in two errors for line 4:

```text
./file.py:4:1: BAS205 missing blank line after "global" statement
./file.py:4:1: BAS104 missing blank line before "del" statement
```

However, two statements of the same type would produce only one "sibling" error.

## Configuration

The plugin checks for blank lines around **every statement**. There are no custom configuration options. Instead, you
could simply ignore some errors. This system has benefits as well as drawbacks.

The benefit is that you could take advantage of Flake8's `ignore` and `per-file-ignores` (flake8 >= 3.7.0) config
options and have a different behaviour for a different set of files:

```ini
[flake8]
ignore = BAS3
per-file-ignores =
    app/*: BAS10, BAS110, BAS20, BAS210
    tests/*: BAS1, BAS2
```

The drawback is that there are no sane defaults and you would inevitably need to exclude some errors, either because
they are undesirable, make little sense, or the same/conflicting checks might already be applied by another plugin
(e.g. checks by [flake8-import-order](https://github.com/PyCQA/flake8-import-order)) or should be handled by other
(formatting) tools (e.g. [black](https://github.com/psf/black)).

### Recommended exclusions

Only compound statements plus `return` and `yield` would raise errors.

```ini
[flake8]
ignore = BAS10, BAS110, BAS20, BAS210, BAS30, BAS310
```

### All simple statements excluded

Only compound statements would raise errors.

```ini
[flake8]
ignore = BAS1, BAS2, BAS3
```

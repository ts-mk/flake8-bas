# Flake8 - check for blank lines around statements

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![PyPI](https://img.shields.io/pypi/v/flake8-bas.svg?label=PyPI&logo=PyPI&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?logo=opensourceinitiative&logoColor=white)
![codecov](https://codecov.io/gh/ts-mk/flake8-bas/branch/master/graph/badge.svg?token=PI2I083V09)
![CI](https://github.com/ts-mk/flake8-bas/actions/workflows/tests.yml/badge.svg)

PEP 8 recommends to use blank lines only to separate logical sections:

> Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between
> a bunch of related one-liners (e.g. a set of dummy implementations).
>
> Use blank lines in functions, sparingly, to indicate logical sections.

However, adding blank lines before and after compound statements (e.g. `if`/`else` block) as well as some simple
statements (e.g. `return`) might improve code readability which is otherwise hindered despite syntax highlighting that
modern code editors provide, as demonstrated in the following example where it might not be immediately apparent that
this is not one `if/else` statement but an `if` statement followed by a `for/else` statement:

```python
if 1 == 1:
    print(1)
for n in [1, 2]:
    print(n)
else:
    print(3)
```

This Flake8 plugin therefore checks for a blank line before/after each statement as long as it's **not the first/last
line of code within a module** and **not the first/last statement within a compound statement**.


## Requirements

* Python >= 3.8
* flake8 >= 3.8.0


## Use in production

Until version 1.0.0 is reached, this plugin is considered as **NOT ready for production**.


## Statements and their error codes

The statements are split into different categories based on whether they are
[simple statements](https://docs.python.org/3.11/reference/simple_stmts.html) or
[compound statements](https://docs.python.org/3.11/reference/compound_stmts.html), and whether the error occurs between
two statements of the same type or not. This allows you to filter entire groups using `BAS` and the first digit,
e.g. `BAS2`.

**Error types:**

* *Before Error* - missing line before a statement as long as the preceding element is not a statement of the same type.
* *After Error* - missing line after a statement as long as the element that follows is not a statement of the same
type.
* *Sibling Error* - missing line between two or more consecutive statements of the same type, e.g. `del`.

### BAS1xx/BAS2xx/BAS3xx: Simple statements

Simple statements, excluding
[expressions](https://docs.python.org/3.11/reference/simple_stmts.html#expression-statements) and
[assignments](https://docs.python.org/3.11/reference/simple_stmts.html#assignment-statements), which are technically
statements as well. "Sibling Error" is used for two or more consecutive statements of the same type, e.g. `del`.

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

**Note:** Some of these errors shouldn't occur (e.g. `return` followed by another `return`) because having consecutive
siblings of those types does not make sense, but the plugin would raise these errors anyway.

### BAS5xx/BAS6xx/BAS7xx: Compound statements

"Sibling Error" is used for two or more consecutive statements of the same type, e.g. `for`.

| Statement    | Before Error | After Error | Sibling Error |
|:-------------|:-------------|:------------|:--------------|
| `async def`  | BAS501       | BAS601      | BAS701        |
| `async for`  | BAS502       | BAS602      | BAS702        |
| `async with` | BAS503       | BAS603      | BAS703        |
| `class`      | BAS504       | BAS604      | BAS704        |
| `def`        | BAS505       | BAS605      | BAS705        |
| `for`        | BAS506       | BAS606      | BAS706        |
| `if`         | BAS507       | BAS607      | BAS707        |
| `match`      | BAS508       | BAS608      | BAS708        |
| `try`        | BAS509       | BAS609      | BAS709        |
| `while`      | BAS510       | BAS610      | BAS710        |
| `with`       | BAS511       | BAS611      | BAS711        |


## Overlapping errors

The extension produces overlapping errors, that is two statements of different types following each other, would produce
one "before" error and one "after" error pointing to the same line of code:

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

The benefit is that you could take advantage of Flake8's `ignore` and `per-file-ignores` (flake8>=3.7.0) config options
and have a different behaviour for a different set of files:

```ini
[flake8]
ignore = BAS2
per-file-ignores =
    app/*: BAS101, BAS102, BAS103, BAS104, BAS105, BAS106, BAS107, BAS108, BAS109, BAS110, BAS201, BAS202, BAS203, BAS204, BAS205, BAS206, BAS207, BAS208, BAS209, BA2110, BAS3
    tests/*: BAS1, BAS2, BAS3
```

The drawback is that there are no sane defaults and you would inevitably need to exclude some errors, either because
they make little sense or because the same/conflicting checks might already be applied by another plugin (e.g. checks by
[flake8-import-order](https://github.com/PyCQA/flake8-import-order)) or should be handled by other (formatting) tools
(e.g. [black](https://github.com/psf/black)).

### Recommended exclusions

Only compound statements plus `return` and `yield` would raise errors.

```ini
[flake8]
ignore = BAS101, BAS102, BAS103, BAS104, BAS105, BAS106, BAS107, BAS108, BAS109, BAS110, BAS201, BAS202, BAS203, BAS204, BAS205, BAS206, BAS207, BAS208, BAS209, BA2110, BAS3
```

### All simple statements excluded

Only compound statements would raise errors.

```ini
[flake8]
ignore = BAS1, BAS2, BAS3
```

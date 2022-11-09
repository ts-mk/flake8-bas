# Flake8 - check for blank lines before statements

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)
![codecov](https://codecov.io/gh/ts-mk/flake8-bbs/branch/initial/graph/badge.svg?token=PI2I083V09)]
![CI](https://github.com/ts-mk/flake8-bbs/actions/workflows/tests.yml/badge.svg)


## Introduction

PEP 8 recommends to use blank lines only to separate logical sections:

> Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).
>
> Use blank lines in functions, sparingly, to indicate logical sections.

However, some people believe that adding blank lines also before (compound) statements improves code readability which is otherwise hindered despite syntax highlighting that modern code editors provide, as demonstrated in the following example:

```python
import os

a = 3
if a == 1:
    print(a)
with os.open('filename.txt') as f:
    content = f.read_lines()
if a == 2:
    print(a)
```

This Flake8 plugin therefore checks for a blank line before each statement as long as it's **not the first line of code within a module** and **not the first statement within another statement**.


## Requirements

* Python >= 3.8
* flake8 >= 3.8.0


## Use in production

Until version 1.0.0 is reached, this plugin is considered as **NOT ready for production**.


## Statements and their error codes

The statements are split into different categories based on whether they are [simple statements](https://docs.python.org/3.11/reference/simple_stmts.html) or [compound statements](https://docs.python.org/3.11/reference/compound_stmts.html) and whether the error occurs between two statements of the same type or not. This allows you to filter entire groups using `BBS` and the first digit, e.g. `BBS3`.

### BBS1xx: Simple statements

Simple statements, excluding [expression statements](https://docs.python.org/3.11/reference/simple_stmts.html#expression-statements) and [assignment statements](https://docs.python.org/3.11/reference/simple_stmts.html#assignment-statements).

| Statement     | Error  |
|:--------------|:-------|
| `assert`      | BBS101 |
| `break`       | BBS102 |
| `continue`    | BBS103 |
| `del`         | BBS104 |
| `global`      | BBS105 |
| `import`      | BBS106 |
| `import from` | BBS107 |
| `nonlocal`    | BBS108 |
| `pass`        | BBS109 |
| `raise`       | BBS110 |
| `return`      | BBS111 |
| `yield`       | BBS112 |
| `yield from`  | BBS113 |


### BBS2xx: Simple statements of the same type

Two or more consecutive simple statements, e.g. `del`. Some of these errors shouldn't occur (e.g. `return` followed by another `return`) because having consecutive siblings of those types does not make sense but the plugin would raise those errors anyway.

| Statement     | Error  |
|:--------------|:-------|
| `assert`      | BBS201 |
| `break`       | BBS202 |
| `continue`    | BBS203 |
| `del`         | BBS204 |
| `global`      | BBS205 |
| `import`      | BBS206 |
| `import from` | BBS207 |
| `nonlocal`    | BBS208 |
| `pass`        | BBS209 |
| `raise`       | BBS210 |
| `return`      | BBS211 |
| `yield`       | BBS212 |
| `yield from`  | BBS213 |

### BBS3xx: Compound statements

| Statement    | Error  |
|:-------------|:-------|
| `async def`  | BBS301 |
| `async for`  | BBS302 |
| `async with` | BBS303 |
| `class`      | BBS304 |
| `def`        | BBS305 |
| `for`        | BBS306 |
| `if`         | BBS307 |
| `match`      | BBS308 |
| `try`        | BBS309 |
| `while`      | BBS310 |
| `with`       | BBS311 |

### BBS4xx: Compound statements of the same type

Two or more consecutive compound statements, e.g. `for`.

| Statement    | Error  |
|:-------------|:-------|
| `async def`  | BBS401 |
| `async for`  | BBS402 |
| `async with` | BBS403 |
| `class`      | BBS404 |
| `def`        | BBS405 |
| `for`        | BBS406 |
| `if`         | BBS407 |
| `match`      | BBS408 |
| `try`        | BBS409 |
| `while`      | BBS410 |
| `with`       | BBS411 |


## Configuration

The plugin checks for a blank line before **every statement**. There are no custom configuration options. Instead, you could simply ignore some errors. This system has benefits as well as drawbacks.

The benefit is that you could take advantage of Flake8's `ignore` and `per-file-ignores` (flake8>=3.7.0) config options and have a different behaviour for a different set of files:

```ini
[flake8]
ignore = BBS2
per-file-ignores =
    app/*: BBS101, BBS102, BBS103, BBS104, BBS105, BBS106, BBS107, BBS109, BBS110
    tests/*: BBS1
```

The drawback is that with more than 40 different errors, there is quite a bit to exclude... and it's certain that you would need to exclude some because the same or conflicting checks might already be applied by another plugin (e.g. checks by [flake8-import-order](https://github.com/PyCQA/flake8-import-order)) or should be handled by other formatting tools (e.g. [black](https://github.com/psf/black)).

### Recommended exclusions

A custom set of what makes sense to the author.

```ini
[flake8]
ignore = BBS101, BBS102, BBS103, BBS104, BBS105, BBS106, BBS107, BBS109, BBS110, BBS2
```

### All simple statements excluded

...so only compound statements would raise errors.

```ini
[flake8]
ignore = BBS1, BBS2
```

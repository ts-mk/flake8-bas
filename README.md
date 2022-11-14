# Flake8 - check for blank lines before statements

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![PyPI](https://img.shields.io/pypi/v/flake8-bbs.svg?label=PyPI&logo=PyPI&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?logo=opensourceinitiative&logoColor=white)
![codecov](https://codecov.io/gh/ts-mk/flake8-bbs/branch/master/graph/badge.svg?token=PI2I083V09)
![CI](https://github.com/ts-mk/flake8-bbs/actions/workflows/tests.yml/badge.svg)

PEP 8 recommends to use blank lines only to separate logical sections:

> Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).
>
> Use blank lines in functions, sparingly, to indicate logical sections.

However, some people believe that adding blank lines before compound statements (e.g. `if`/`else` block) and some simple statements (e.g. `return`) improves code readability which is otherwise hindered despite syntax highlighting that modern code editors provide, as demonstrated in the following example:

```python
a = 1
b = 2
if a == 1:
    print(a)
for n in range(10):
    print(n)
return a
```

This Flake8 plugin therefore checks for a blank line before each statement as long as it's **not the first line of code within a module** and **not the first statement within a compound statement**.


## Requirements

* Python >= 3.8
* flake8 >= 3.8.0


## Use in production

Until version 1.0.0 is reached, this plugin is considered as **NOT ready for production**.


## Statements and their error codes

The statements are split into different categories based on whether they are [simple statements](https://docs.python.org/3.11/reference/simple_stmts.html) or [compound statements](https://docs.python.org/3.11/reference/compound_stmts.html), and whether the error occurs between two statements of the same type or not. This allows you to filter entire groups using `BBS` and the first digit, e.g. `BBS3`.

### BBS1xx/BBS2xx: Simple statements

Simple statements, excluding [expressions](https://docs.python.org/3.11/reference/simple_stmts.html#expression-statements) and [assignments](https://docs.python.org/3.11/reference/simple_stmts.html#assignment-statements) which are technically statements as well. "Sibling Error" is used for two or more consecutive statements of the same type, e.g. `del`.

| Statement         | Error  | Sibling Error |
|:------------------|:-------|:--------------|
| `assert`          | BBS101 | BBS201        |
| `break`           | BBS102 | BBS202        |
| `continue`        | BBS103 | BBS203        |
| `del`             | BBS104 | BBS204        |
| `global`          | BBS105 | BBS205        |
| `import`          | BBS106 | BBS206        |
| `from import`     | BBS107 | BBS207        |
| `nonlocal`        | BBS108 | BBS208        |
| `pass`            | BBS109 | BBS209        |
| `raise`           | BBS110 | BBS210        |
| `return`          | BBS111 | BBS211        |
| `yield`           | BBS112 | BBS212        |
| `yield from`      | BBS113 | BBS213        |

**Note:** Some of these errors shouldn't occur (e.g. `return` followed by another `return`) because having consecutive siblings of those types does not make sense, but the plugin would raise these errors anyway.

### BBS3xx/BBS4xx: Compound statements

"Sibling Error" is used for two or more consecutive statements of the same type, e.g. `for`.

| Statement    | Error  | Sibling Error |
|:-------------|:-------|:--------------|
| `async def`  | BBS301 | BBS401        |
| `async for`  | BBS302 | BBS402        |
| `async with` | BBS303 | BBS403        |
| `class`      | BBS304 | BBS404        |
| `def`        | BBS305 | BBS405        |
| `for`        | BBS306 | BBS406        |
| `if`         | BBS307 | BBS407        |
| `match`      | BBS308 | BBS408        |
| `try`        | BBS309 | BBS409        |
| `while`      | BBS310 | BBS410        |
| `with`       | BBS311 | BBS411        |


## Configuration

The plugin checks for a blank line before **every statement**. There are no custom configuration options. Instead, you could simply ignore some errors. This system has benefits as well as drawbacks.

The benefit is that you could take advantage of Flake8's `ignore` and `per-file-ignores` (flake8>=3.7.0) config options and have a different behaviour for a different set of files:

```ini
[flake8]
ignore = BBS2
per-file-ignores =
    app/*: BBS101, BBS102, BBS103, BBS104, BBS105, BBS106, BBS107, BBS108, BBS109, BBS110, BBS2
    tests/*: BBS1, BBS2
```

The drawback is that there are no sane defaults and you would inevitably need to exclude some errors, either because they make little sense or because the same/conflicting checks might already be applied by another plugin (e.g. checks by [flake8-import-order](https://github.com/PyCQA/flake8-import-order)) or should be handled by other formatting tools (e.g. [black](https://github.com/psf/black)).

### Recommended exclusions

Only compound statements plus `return` and `yield` would raise errors.

```ini
[flake8]
ignore = BBS101, BBS102, BBS103, BBS104, BBS105, BBS106, BBS107, BBS108, BBS109, BBS110, BBS2
```

### All simple statements excluded

Only compound statements would raise errors.

```ini
[flake8]
ignore = BBS1, BBS2
```

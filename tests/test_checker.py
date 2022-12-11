import ast
from collections import OrderedDict
from typing import Callable

import pytest

from flake8_bas.checker import StatementChecker


@pytest.mark.parametrize(
    "value, expected",
    (
        ("\n", True),
        (" \n", True),
        ("\t\n", True),
        (" # \n", False),
    ),
)
def test_blank_line_regex(value: str, expected: bool):
    assert (StatementChecker.BLANK_LINE_RE.match(value) is not None) is expected


def test_indexed_tree(file_fixture: Callable):
    tree = ast.parse(file_fixture("indexed_tree.py").read_text())
    indexed_tree = StatementChecker._indexed_tree(tree)
    counter_index = 0

    assert isinstance(indexed_tree, OrderedDict)

    for index, node in indexed_tree.items():
        assert index == counter_index
        assert node.index == counter_index

        counter_index += 1


@pytest.mark.parametrize(
    "statement, equal, real_node_cls",
    (
        (ast.FunctionDef, True, ast.FunctionDef),
        (ast.Expr, False, ast.Yield),
    ),
)
def test_real_node(
    statement: type, equal: bool, real_node_cls: type, file_fixture: Callable
):
    tree = ast.parse(file_fixture("real_node.py").read_text())
    nodes = list(StatementChecker._indexed_tree(tree).values())
    node = list(filter(lambda n: isinstance(n, statement), nodes))[0]
    result = StatementChecker._real_node(node)

    assert (result is node) is equal
    assert isinstance(result, real_node_cls)


@pytest.mark.parametrize(
    "statement, index",
    (
        (ast.Assert, 0),
        (ast.Import, 1),
        (ast.Pass, 2),
        (ast.Pass, -1),
    ),
)
def test_is_nth_child(statement: type, index: int, file_fixture: Callable):
    tree = ast.parse(file_fixture("nth_child.py").read_text())
    nodes = list(StatementChecker._indexed_tree(tree).values())
    node = list(filter(lambda n: isinstance(n, statement), nodes))[0]

    assert StatementChecker._is_nth_child(node, index)

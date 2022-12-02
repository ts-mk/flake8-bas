import ast
import re
from collections import OrderedDict
from dataclasses import dataclass, astuple
from typing import Generator, List, Optional, NamedTuple, Tuple

import pkg_resources


@dataclass(init=False, frozen=True)
class StatementErrors:
    """
    Statement's error codes.
    """

    ERROR_NAMESPACE = "BAS"

    after: str
    before: str
    sibling: str

    def __init__(self, before: int, after: int, sibling: int) -> None:
        """
        :param before: error number for a missing blank line before a statement
        :param after: error number for a missing blank line after a statement
        :param sibling: error number for a missing blank between sibling statements
        """
        self.__dict__["before"] = f"{self.ERROR_NAMESPACE}{before}"
        self.__dict__["after"] = f"{self.ERROR_NAMESPACE}{after}"
        self.__dict__["sibling"] = f"{self.ERROR_NAMESPACE}{sibling}"

    def __len__(self) -> int:
        """
        Returns number of the errors.

        :return: length
        """
        return len(self.__dict__)

    def to_tuple(self) -> tuple:
        """
        Turns the object into a tuple.

        :return: tuple of error codes
        """
        return astuple(self)


@dataclass(frozen=True)
class Statement:
    """
    Python's statement data.
    """

    keyword: str
    cls: type
    errors: StatementErrors
    python_compatibility: Tuple[int, int]


class Error(NamedTuple):
    """
    Describes an error in the form of a tuple that Flake8 expects.
    """

    lineno: int
    col_offset: int
    message: str
    checker_type: type


SIMPLE_STATEMENTS = (
    Statement(
        "assert",
        ast.Assert,
        StatementErrors(101, 201, 301),
        (3, 5),
    ),
    Statement(
        "break",
        ast.Break,
        StatementErrors(102, 202, 302),
        (3, 5),
    ),
    Statement(
        "continue",
        ast.Continue,
        StatementErrors(103, 203, 303),
        (3, 5),
    ),
    Statement(
        "del",
        ast.Delete,
        StatementErrors(104, 204, 304),
        (3, 5),
    ),
    Statement(
        "global",
        ast.Global,
        StatementErrors(105, 205, 305),
        (3, 5),
    ),
    Statement(
        "import",
        ast.Import,
        StatementErrors(106, 206, 306),
        (3, 5),
    ),
    Statement(
        "from import",
        ast.ImportFrom,
        StatementErrors(107, 207, 307),
        (3, 5),
    ),
    Statement(
        "nonlocal",
        ast.Nonlocal,
        StatementErrors(108, 208, 308),
        (3, 5),
    ),
    Statement(
        "pass",
        ast.Pass,
        StatementErrors(109, 209, 309),
        (3, 5),
    ),
    Statement(
        "raise",
        ast.Raise,
        StatementErrors(110, 210, 310),
        (3, 5),
    ),
    Statement(
        "return",
        ast.Return,
        StatementErrors(111, 211, 311),
        (3, 5),
    ),
    Statement(
        "yield",
        ast.Yield,
        StatementErrors(112, 212, 312),
        (3, 5),
    ),
    Statement(
        "yield from",
        ast.YieldFrom,
        StatementErrors(113, 213, 313),
        (3, 5),
    ),
)
COMPOUND_STATEMENTS = (
    Statement(
        "async def",
        ast.AsyncFunctionDef,
        StatementErrors(501, 601, 701),
        (3, 5),
    ),
    Statement(
        "async for",
        ast.AsyncFor,
        StatementErrors(502, 602, 702),
        (3, 5),
    ),
    Statement(
        "async with",
        ast.AsyncWith,
        StatementErrors(503, 603, 703),
        (3, 5),
    ),
    Statement(
        "class",
        ast.ClassDef,
        StatementErrors(504, 604, 704),
        (3, 5),
    ),
    Statement(
        "def",
        ast.FunctionDef,
        StatementErrors(505, 605, 705),
        (3, 5),
    ),
    Statement(
        "for",
        ast.For,
        StatementErrors(506, 606, 706),
        (3, 5),
    ),
    Statement(
        "if",
        ast.If,
        StatementErrors(507, 607, 707),
        (3, 5),
    ),
    Statement(
        "match",
        getattr(ast, "Match", None),
        StatementErrors(508, 608, 708),
        (3, 10),
    ),
    Statement(
        "try",
        ast.Try,
        StatementErrors(509, 609, 709),
        (3, 5),
    ),
    Statement(
        "while",
        ast.While,
        StatementErrors(510, 610, 710),
        (3, 5),
    ),
    Statement(
        "with",
        ast.With,
        StatementErrors(511, 611, 711),
        (3, 5),
    ),
)
STATEMENTS = SIMPLE_STATEMENTS + COMPOUND_STATEMENTS


class StatementChecker:
    """
    Checks for blank lines before statements.
    """

    BLANK_LINE_RE = re.compile(r"^\s*\n")

    name = "flake8-bas"
    version = pkg_resources.get_distribution(name).version

    def __init__(self, tree: ast.Module, lines: List[str]) -> None:
        """
        :param tree: parsed abstract syntax tree of a module
        :param lines: module's lines of code
        """
        self.statement_map = {s.cls: s for s in STATEMENTS if s.cls}
        self.tree = self._indexed_tree(tree)
        self.blank_lines = [
            lineno
            for lineno, line in enumerate(lines, start=1)
            if self.BLANK_LINE_RE.match(line)
        ]

    @classmethod
    def _indexed_tree(cls, module_tree: ast.Module) -> OrderedDict:
        """
        Takes an AST tree and turns it into an ordered dict with each node having
        an index number.

        :param module_tree: AST tree
        :return: nodes with index
        """
        tree = OrderedDict()

        for index, node in enumerate(ast.walk(module_tree)):
            for child in ast.iter_child_nodes(node):
                child.parent_node = node

            node.index = index
            tree[index] = node

        return tree

    @classmethod
    def _real_node(cls, node: ast.AST) -> ast.AST:
        """
        Returns "real" class of a node - some nodes might be wrapped in other nodes
        while for instance comparison we need to determine the inner node's class.

        :param node: AST node
        :return: AST node class
        """
        if isinstance(node, ast.Expr) and isinstance(
            getattr(node, "value", None), (ast.Yield, ast.YieldFrom)
        ):
            return node.value
        else:
            return node

    @classmethod
    def _is_nth_child(cls, node: ast.AST, n: int) -> bool:
        """
        Checks if the node is the Nth child within its parent.

        :param node: AST node
        :param n: index within a list
        :return: True if it is, otherwise False
        """
        if not (parent_node := getattr(node, "parent_node", None)):
            return False

        if len(getattr(parent_node, "body", [])) and parent_node.body[n] is node:
            return True

        if len(getattr(parent_node, "orelse", [])) and parent_node.orelse[n] is node:
            return True

        return False

    def _error_before(self, node: ast.AST, on_behalf_of: ast.AST) -> Optional[Error]:
        """
        Checks for an error before the statement.

        :param node: AST node
        :param on_behalf_of: original node to be evaluated
        :return: error code
        """
        previous_node: ast.AST = self.tree.get(node.index - 1)

        # A (string) constant expression is allowed to be directly above the node
        # but then it needs to match all the other rules so we need to do
        # a look behind (or rather above)
        if (
            previous_node
            and isinstance(previous_node, ast.Expr)
            and isinstance(getattr(previous_node, "value", None), ast.Constant)
        ):
            return self._error_before(node=previous_node, on_behalf_of=on_behalf_of)

        # Blank line found above the statement
        if (
            previous_node
            and getattr(previous_node, "end_lineno", None)
            and any(
                line in self.blank_lines
                for line in range(previous_node.end_lineno, node.lineno)
            )
        ):
            return

        # If the node is a first child of a compound statement, it doesn't need
        # a blank line
        if self._is_nth_child(node=node, n=0):
            return

        # All valid conditions exhausted so return an error
        keyword = self.statement_map[on_behalf_of.__class__].keyword

        if previous_node and isinstance(
            on_behalf_of, self._real_node(previous_node).__class__
        ):
            error_code = self.statement_map[on_behalf_of.__class__].errors.sibling
        else:
            error_code = self.statement_map[on_behalf_of.__class__].errors.before

        return Error(
            node.lineno,
            node.col_offset,
            f'{error_code} missing blank line before "{keyword}" statement',
            type(self),
        )

    def _error_after(self, node: ast.AST, on_behalf_of: ast.AST) -> Optional[Error]:
        """
        Checks for an error after the statement.

        :param node: AST node
        :param on_behalf_of: original node to be evaluated
        :return: error code
        """
        next_node = self.tree.get(node.index + 1)

        # If the node is the last node in the module, dismiss it
        if node is self.tree[next(reversed(self.tree))]:
            return

        # If the node is a first child of a compound statement, it doesn't need
        # a blank line
        if self._is_nth_child(node=node, n=-1):
            return

        # Blank line found below the statement
        if (
            getattr(node, "end_lineno", None)
            and node.end_lineno + 1 in self.blank_lines
        ):
            return

        # If the next node is a statement, then we could dismiss it
        # because the next item would raise an error itself
        if next_node and isinstance(
            self._real_node(next_node), tuple(self.statement_map.keys())
        ):
            return

        # All valid conditions exhausted so return an error
        error_code = self.statement_map[on_behalf_of.__class__].errors.after
        keyword = self.statement_map[on_behalf_of.__class__].keyword

        return Error(
            next_node.lineno,
            next_node.col_offset,
            f'{error_code} missing blank line after "{keyword}" statement',
            type(self),
        )

    def _node_error(
        self, node: ast.AST, on_behalf_of: Optional[ast.AST] = None
    ) -> Optional[Error]:
        """
        Checks whether the node is valid or not.

        :param node: AST node
        :param on_behalf_of: original node to be evaluated
        :return: error code
        """
        on_behalf_of = on_behalf_of or node
        parent_node = getattr(node, "parent_node", None)

        # Non-statement objects should be dismissed
        if not isinstance(on_behalf_of, tuple(self.statement_map.keys())):
            return

        # First line of code could be dismissed
        if getattr(node, "lineno", None) == 1:
            return

        # `yield (from)` is a bit of an oddball - it's always "wrapped" in ast.Expr
        # so we need to check that instead
        if (
            parent_node
            and isinstance(node, (ast.Yield, ast.YieldFrom))
            and isinstance(parent_node, ast.Expr)
            and getattr(parent_node, "value", None) is node
        ):
            return self._node_error(node=parent_node, on_behalf_of=on_behalf_of)

        if error := self._error_before(node=node, on_behalf_of=on_behalf_of):
            return error
        elif error := self._error_after(node=node, on_behalf_of=on_behalf_of):
            return error

    def run(self) -> Generator[Error, None, None]:
        """
        Searches the abstract syntax tree of a module and yields an error for each
        invalid statement.

        :return: error generator
        """
        for node in self.tree.values():
            if error := self._node_error(node=node):
                yield error

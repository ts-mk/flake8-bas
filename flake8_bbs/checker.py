import argparse
import ast
import re
from typing import Generator, List, NamedTuple, Optional, Tuple

import pkg_resources


class Statement(NamedTuple):
    """
    Python statement definition
    """

    keyword: str
    cls: type
    error_code: str
    sibling_error_code: str
    python_compatibility: Tuple[int, int]


class Error(NamedTuple):
    """
    Error item
    """

    lineno: int
    col_offset: int
    message: str
    checker_type: type


ERROR_NAMESPACE = "BBS"
SIMPLE_STATEMENTS = (
    Statement(
        "assert",
        ast.Assert,
        f"{ERROR_NAMESPACE}101",
        f"{ERROR_NAMESPACE}201",
        (3, 5),
    ),
    Statement(
        "break",
        ast.Break,
        f"{ERROR_NAMESPACE}102",
        f"{ERROR_NAMESPACE}202",
        (3, 5),
    ),
    Statement(
        "continue",
        ast.Continue,
        f"{ERROR_NAMESPACE}103",
        f"{ERROR_NAMESPACE}203",
        (3, 5),
    ),
    Statement(
        "del",
        ast.Delete,
        f"{ERROR_NAMESPACE}104",
        f"{ERROR_NAMESPACE}204",
        (3, 5),
    ),
    Statement(
        "global",
        ast.Global,
        f"{ERROR_NAMESPACE}105",
        f"{ERROR_NAMESPACE}205",
        (3, 5),
    ),
    Statement(
        "import",
        ast.Import,
        f"{ERROR_NAMESPACE}106",
        f"{ERROR_NAMESPACE}206",
        (3, 5),
    ),
    Statement(
        "import from",
        ast.ImportFrom,
        f"{ERROR_NAMESPACE}107",
        f"{ERROR_NAMESPACE}207",
        (3, 5),
    ),
    Statement(
        "nonlocal",
        ast.Nonlocal,
        f"{ERROR_NAMESPACE}108",
        f"{ERROR_NAMESPACE}208",
        (3, 5),
    ),
    Statement(
        "pass",
        ast.Pass,
        f"{ERROR_NAMESPACE}109",
        f"{ERROR_NAMESPACE}209",
        (3, 5),
    ),
    Statement(
        "raise",
        ast.Raise,
        f"{ERROR_NAMESPACE}110",
        f"{ERROR_NAMESPACE}210",
        (3, 5),
    ),
    Statement(
        "return",
        ast.Return,
        f"{ERROR_NAMESPACE}111",
        f"{ERROR_NAMESPACE}211",
        (3, 5),
    ),
    Statement(
        "yield",
        ast.Yield,
        f"{ERROR_NAMESPACE}112",
        f"{ERROR_NAMESPACE}212",
        (3, 5),
    ),
    Statement(
        "yield from",
        ast.YieldFrom,
        f"{ERROR_NAMESPACE}113",
        f"{ERROR_NAMESPACE}213",
        (3, 5),
    ),
)
COMPOUND_STATEMENTS = (
    Statement(
        "async def",
        ast.AsyncFunctionDef,
        f"{ERROR_NAMESPACE}301",
        f"{ERROR_NAMESPACE}401",
        (3, 5),
    ),
    Statement(
        "async for",
        ast.AsyncFor,
        f"{ERROR_NAMESPACE}302",
        f"{ERROR_NAMESPACE}402",
        (3, 5),
    ),
    Statement(
        "async with",
        ast.AsyncWith,
        f"{ERROR_NAMESPACE}303",
        f"{ERROR_NAMESPACE}403",
        (3, 5),
    ),
    Statement(
        "class",
        ast.ClassDef,
        f"{ERROR_NAMESPACE}304",
        f"{ERROR_NAMESPACE}404",
        (3, 5),
    ),
    Statement(
        "def",
        ast.FunctionDef,
        f"{ERROR_NAMESPACE}305",
        f"{ERROR_NAMESPACE}405",
        (3, 5),
    ),
    Statement(
        "for",
        ast.For,
        f"{ERROR_NAMESPACE}306",
        f"{ERROR_NAMESPACE}406",
        (3, 5),
    ),
    Statement(
        "if",
        ast.If,
        f"{ERROR_NAMESPACE}307",
        f"{ERROR_NAMESPACE}407",
        (3, 5),
    ),
    Statement(
        "match",
        getattr(ast, "Match", None),
        f"{ERROR_NAMESPACE}308",
        f"{ERROR_NAMESPACE}408",
        (3, 10),
    ),
    Statement(
        "try",
        ast.Try,
        f"{ERROR_NAMESPACE}309",
        f"{ERROR_NAMESPACE}409",
        (3, 5),
    ),
    Statement(
        "while",
        ast.While,
        f"{ERROR_NAMESPACE}310",
        f"{ERROR_NAMESPACE}410",
        (3, 5),
    ),
    Statement(
        "with",
        ast.With,
        f"{ERROR_NAMESPACE}311",
        f"{ERROR_NAMESPACE}411",
        (3, 5),
    ),
)
STATEMENTS = SIMPLE_STATEMENTS + COMPOUND_STATEMENTS


class StatementChecker:
    """
    Checks for blank lines before statements.
    """

    BLANK_LINE_RE = re.compile(r"^\s*\n")

    name = "flake8-bbs"
    version = pkg_resources.get_distribution(name).version
    options = None

    def __init__(self, tree: ast.Module, lines: List[str]) -> None:
        """
        :param tree: parsed abstract syntax tree of a module
        :param lines: module's lines of code
        """
        self.statement_map = {s.cls: s for s in STATEMENTS if s.cls}
        self.tree = tree
        self.blank_lines = [
            lineno
            for lineno, line in enumerate(lines, start=1)
            if self.BLANK_LINE_RE.match(line)
        ]

    @classmethod
    def parse_options(cls, options: argparse.Namespace) -> None:
        """
        Sets Flake8's options.

        :param options: list of options
        """
        cls.options = options

    def _node_invalid(self, node: ast.AST) -> Optional[str]:
        """
        Checks whether the node is valid or not.

        :param node: AST node
        :return: error code
        """
        previous_node = getattr(node, "previous_node", None)

        if not isinstance(node, tuple(self.statement_map.keys())):
            return

        if node.lineno == 1:
            return

        if (
            previous_node
            and getattr(previous_node, "end_lineno", None)
            and any(
                line in self.blank_lines
                for line in range(previous_node.end_lineno, node.lineno)
            )
        ):
            return

        if self._is_first_child(node):
            return

        if previous_node and isinstance(previous_node, ast.Expr):
            return

        # All valida conditions exhausted so return an error
        if previous_node and isinstance(node, previous_node.__class__):
            return self.statement_map[node.__class__].sibling_error_code
        else:
            return self.statement_map[node.__class__].error_code

    @classmethod
    def _is_first_child(cls, node: ast.AST) -> bool:
        """
        Checks if the node is the first child within its parent.

        :param node: AST node
        :return: True if it is, otherwise False
        """
        if not (parent_node := getattr(node, "parent_node", None)):
            return False

        if len(getattr(parent_node, "body", [])) and parent_node.body[0] is node:
            return True

        if len(getattr(parent_node, "orelse", [])) and parent_node.orelse[0] is node:
            return True

        return False

    @classmethod
    def _prepare_node(
        cls, node: ast.AST, previous_node: Optional[ast.AST] = None
    ) -> None:
        """
        Prepares the  node for further use.

        :param node: AST node
        :param previous_node: previously found node
        """
        node.previous_node = previous_node

        for child in ast.iter_child_nodes(node):
            child.parent_node = node

    def run(self) -> Generator[Error, None, None]:
        """
        Searches the abstract syntax tree of a module and yields an error for each
        invalid statement.

        :return: error generator
        """
        previous_node = None

        for node in ast.walk(self.tree):
            self._prepare_node(node=node, previous_node=previous_node)

            if error_code := self._node_invalid(node=node):
                yield Error(
                    node.lineno,
                    node.col_offset,
                    f"{error_code} missing blank line before "
                    f'"{self.statement_map[node.__class__].keyword}" statement',
                    type(self),
                )

            previous_node = node

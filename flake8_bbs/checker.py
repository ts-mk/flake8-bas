import argparse
import ast
import re
from collections import namedtuple
from typing import Generator, List, Optional

import pkg_resources

Statement = namedtuple("Statement", ["keyword", "cls", "error_code"])
Error = namedtuple("Error", ["lineno", "col_offset", "message", "type"])


class StatementChecker:
    """
    Checks for blank lines before statements.
    """

    BLANK_LINE_RE = re.compile(r"^\s*\n")
    ERROR_NAMESPACE = "BBS"
    STATEMENTS = (
        Statement("assert", ast.Assert, f"{ERROR_NAMESPACE}010"),
        Statement("async for", ast.AsyncFor, f"{ERROR_NAMESPACE}020"),
        Statement("async def", ast.AsyncFunctionDef, f"{ERROR_NAMESPACE}030"),
        Statement("async with", ast.AsyncWith, f"{ERROR_NAMESPACE}040"),
        Statement("break", ast.Break, f"{ERROR_NAMESPACE}050"),
        Statement("class", ast.ClassDef, f"{ERROR_NAMESPACE}060"),
        Statement("continue", ast.Continue, f"{ERROR_NAMESPACE}070"),
        Statement("del", ast.Delete, f"{ERROR_NAMESPACE}080"),
        Statement("for", ast.For, f"{ERROR_NAMESPACE}090"),
        Statement("def", ast.FunctionDef, f"{ERROR_NAMESPACE}100"),
        Statement("global", ast.Global, f"{ERROR_NAMESPACE}110"),
        Statement("if", ast.If, f"{ERROR_NAMESPACE}120"),
        Statement("import", ast.Import, f"{ERROR_NAMESPACE}130"),
        Statement("import from", ast.ImportFrom, f"{ERROR_NAMESPACE}140"),
        Statement("nonlocal", ast.Nonlocal, f"{ERROR_NAMESPACE}150"),
        Statement("pass", ast.Pass, f"{ERROR_NAMESPACE}160"),
        Statement("raise", ast.Raise, f"{ERROR_NAMESPACE}170"),
        Statement("return", ast.Return, f"{ERROR_NAMESPACE}180"),
        Statement("try", ast.Try, f"{ERROR_NAMESPACE}190"),
        Statement("while", ast.While, f"{ERROR_NAMESPACE}200"),
        Statement("with", ast.With, f"{ERROR_NAMESPACE}210"),
        Statement("yield", ast.Yield, f"{ERROR_NAMESPACE}220"),
        Statement("yield from", ast.YieldFrom, f"{ERROR_NAMESPACE}230"),
    )

    name = "flake8-bbs"
    version = pkg_resources.get_distribution(name).version
    options = None

    def __init__(
        self,
        filename: str,
        tree: Optional[ast.Module] = None,
        lines: Optional[List[str]] = None,
    ) -> None:
        """
        :param filename: filename of the module
        :param tree: parsed abstract syntax tree of a module
        :param lines: module's lines of code
        """
        self.statement_map = {s.cls: s for s in self.STATEMENTS}
        self.tree = tree
        self.filename = filename
        self.blank_lines = [
            lineno
            for lineno, line in enumerate(lines, start=1)
            if self.BLANK_LINE_RE.match(line)
        ]

    @classmethod
    def parse_options(cls, options: argparse.Namespace) -> None:
        """
        Sets Flake8 options.

        :param options: list of options
        """
        cls.options = options

    def _node_invalid(self, node: ast.AST) -> bool:
        """
        Checks whether the node is valid or not.

        :param node: AST node
        :return: True if the node passes the checks, otherwise False
        """
        previous_node = getattr(node, "previous_node", None)

        if not isinstance(node, tuple(self.statement_map.keys())):
            return False

        if node.lineno == 1:
            return False

        if (
            previous_node
            and getattr(previous_node, "end_lineno", None)
            and any(
                line in self.blank_lines
                for line in range(previous_node.end_lineno, node.lineno)
            )
        ):
            return False

        if self._is_first_child(node):
            return False

        if previous_node and isinstance(previous_node, ast.Expr):
            return False

        return True

    def _is_first_child(self, node: ast.AST) -> bool:
        """
        Checks if the node is the first child within its parent.

        :param node: AST node
        :return: True if it is, otherwise False
        """
        parent_node = getattr(node, "parent_node", None)

        if not parent_node:
            return False

        if len(getattr(parent_node, "body", [])) and parent_node.body[0] is node:
            return True

        if len(getattr(parent_node, "orelse", [])) and parent_node.orelse[0] is node:
            return True

        return False

    def _prepare_node(
        self, node: ast.AST, previous_node: Optional[ast.AST] = None
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

            if self._node_invalid(node=node):
                yield Error(
                    node.lineno,
                    node.col_offset,
                    f"{self.statement_map[node.__class__].error_code} "
                    f"missing blank line before "
                    f'"{self.statement_map[node.__class__].keyword}" statement',
                    type(self),
                )

            previous_node = node

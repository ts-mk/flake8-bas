import ast
import re
import sys
from pathlib import Path
from typing import Callable, NamedTuple, Tuple

import pytest
from _pytest.fixtures import SubRequest

from flake8_bbs.checker import Error, STATEMENTS, StatementChecker


class CheckerTester(NamedTuple):
    file: Path
    checker: StatementChecker
    error_codes: Tuple[str, ...]
    error_count: int


FILE_FORMAT = re.compile(r"([a-z\s]+)\-?(\d*)")
TEST_ROOT = Path(__file__).parent


def load_files(subdirectory: str) -> list[Path]:
    """
    Loads files fixtures subdirectory taking into account whether the statement exists
    in the current version of Python.

    :param subdirectory: subdirectory name
    :return: list of files
    """
    output = []

    for file in (TEST_ROOT / f"fixtures/{subdirectory}").rglob("*.py"):
        match = FILE_FORMAT.match(file.stem)

        for statement in STATEMENTS:
            if (
                match.groups()[0] == statement.keyword
                and sys.version_info >= statement.python_compatibility
            ):
                output.append(file)

    return output


def errors_from_file(file: Path) -> Tuple[str, ...]:
    """
    Resolves the package's Flake8 error codes based on the file's name.

    :param file: file object
    :return: error code
    """
    try:
        match = FILE_FORMAT.match(file.stem)

        for statement in STATEMENTS:
            if match.groups()[0] == statement.keyword:
                return (statement.error_code, statement.sibling_error_code)
        else:
            raise Exception
    except Exception as e:
        raise Exception("Statement not found for the given filename") from e


def error_count_from_file(file: Path) -> int:
    """
    Determines number of expected errors based on the file's name.

    :param file: file object
    :return: error count
    """
    match = FILE_FORMAT.match(file.stem)

    return int(match.groups()[1]) if match else 0


@pytest.fixture()
def error_formatter() -> Callable:
    """
    Returns a function that can be used to format an error string.

    :return: function
    """

    def _(file: Path, errors: list[Error]) -> str:
        return ", ".join(f"{file.name}:{e.lineno}:{e.col_offset}" for e in errors)

    return _


@pytest.fixture(params=load_files("valid"))
def valid(request: SubRequest) -> CheckerTester:
    """
    Returns StatementChecker context for one of the valid fixture files.

    :param request: fixture request instance
    :return: tester
    """
    content = request.param.read_text()

    return CheckerTester(
        request.param,
        StatementChecker(
            tree=ast.parse(content),
            lines=[f"{line}\n" for line in content.split("\n")],
        ),
        errors_from_file(request.param),
        0,
    )


@pytest.fixture(params=load_files("invalid"))
def invalid(request: SubRequest) -> CheckerTester:
    """
    Returns StatementChecker context for one of the invalid fixture files.

    :param request: fixture request instance
    :return: tester
    """
    content = request.param.read_text()

    return CheckerTester(
        request.param,
        StatementChecker(
            tree=ast.parse(content),
            lines=[f"{line}\n" for line in content.split("\n")],
        ),
        errors_from_file(request.param),
        error_count_from_file(request.param),
    )

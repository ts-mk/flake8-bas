import ast
import re
import sys
from pathlib import Path
from typing import List, NamedTuple, Optional, Tuple

import pytest
from _pytest.fixtures import SubRequest

from flake8_bbs.checker import STATEMENTS, StatementChecker


class StatementTest(NamedTuple):
    file: Path
    checker: StatementChecker
    error_codes: Tuple[str, ...]
    error_count: int


FILE_FORMAT = re.compile(r"([a-z_]+)\-?(\d*)")
STATEMENT_MAP = {s.keyword: s for s in STATEMENTS}
TEST_ROOT = Path(__file__).parent


def load_files(subdirectory: Optional[str] = "") -> List[Path]:
    """
    Loads files fixtures subdirectory taking into account whether the statement exists
    in the current version of Python.

    :param subdirectory: subdirectory name
    :return: list of files
    """
    output = []

    for file in (TEST_ROOT / "fixtures" / subdirectory).rglob("*.py"):
        match = FILE_FORMAT.match(file.stem)
        statement = STATEMENT_MAP[match.groups()[0].replace("_", " ")]

        if sys.version_info >= statement.python_compatibility:
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
        statement = STATEMENT_MAP[match.groups()[0].replace("_", " ")]

        return (statement.error_code, statement.sibling_error_code)
    except Exception as e:
        raise Exception("Statement not found for the given filename") from e


def error_count_from_file(file: Path) -> int:
    """
    Determines number of expected errors based on the file's name.

    :param file: file object
    :return: error count
    """
    match = FILE_FORMAT.match(file.stem)

    try:
        return int(match.groups()[1])
    except Exception:
        return 0


@pytest.fixture()
def statement_test(request: SubRequest) -> StatementTest:
    """
    Returns a StatementTest for the given file.

    :return: function
    """
    content = request.param.read_text()

    return StatementTest(
        request.param,
        StatementChecker(
            tree=ast.parse(content),
            lines=[f"{line}\n" for line in content.split("\n")],
        ),
        errors_from_file(request.param),
        error_count_from_file(request.param),
    )

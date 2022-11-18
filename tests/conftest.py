import ast
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import pytest
from _pytest.fixtures import SubRequest

from flake8_bas.checker import STATEMENTS, Statement, StatementChecker


@dataclass(frozen=True)
class StatementTest:
    file: Path
    checker: StatementChecker
    statement: Statement
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

    for file in sorted((TEST_ROOT / "fixtures" / subdirectory).rglob("*.py")):
        match = FILE_FORMAT.match(file.stem)
        statement = STATEMENT_MAP[match.groups()[0].replace("_", " ")]

        if sys.version_info >= statement.python_compatibility:
            output.append(file)

    return output


def statement_from_file(file: Path) -> Statement:
    """
    Resolves the package's Flake8 error codes based on the file's name.

    :param file: file object
    :return: error code
    """
    try:
        match = FILE_FORMAT.match(file.stem)

        return STATEMENT_MAP[match.groups()[0].replace("_", " ")]
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
        statement_from_file(request.param),
        error_count_from_file(request.param),
    )

import ast
import re
from collections import namedtuple
from pathlib import Path
from typing import Callable

import pytest

from flake8_bbs import StatementChecker

CheckerTester = namedtuple(
    "CheckerTester", ["file", "checker", "error_code", "error_count"]
)

FILE_FORMAT = re.compile(r"([a-z\s]+)\-?(\d*)")


def error_from_file(file: Path) -> str:
    try:
        match = FILE_FORMAT.match(file.stem)

        for statement in StatementChecker.STATEMENTS:
            if match.groups()[0] == statement.keyword:
                return statement.error_code
        else:
            raise Exception
    except Exception as e:
        raise Exception("Statement not found for the given filename") from e


def error_count_from_file(file: Path) -> int:
    match = FILE_FORMAT.match(file.stem)

    return int(match.groups()[1]) if match else 0


@pytest.fixture()
def error_compiler() -> Callable:
    def _(file: Path, errors: list):
        return ", ".join(f"{file.name}:{e.lineno}:{e.col_offset}" for e in errors)

    return _


@pytest.fixture(params=(Path(__file__).parent / "fixtures/valid").glob("*.py"))
def valid(request) -> CheckerTester:
    content = request.param.read_text()

    return CheckerTester(
        request.param,
        StatementChecker(
            filename=str(request.param),
            tree=ast.parse(content),
            lines=[f"{l}\n" for l in content.split("\n")],
        ),
        error_from_file(request.param),
        0,
    )


@pytest.fixture(params=(Path(__file__).parent / "fixtures/invalid").glob("*.py"))
def invalid(request) -> CheckerTester:
    content = request.param.read_text()

    return CheckerTester(
        request.param,
        StatementChecker(
            filename=str(request.param),
            tree=ast.parse(content),
            lines=[f"{l}\n" for l in content.split("\n")],
        ),
        error_from_file(request.param),
        error_count_from_file(request.param),
    )

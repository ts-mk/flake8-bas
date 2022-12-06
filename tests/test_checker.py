import re
from pathlib import Path
from typing import Callable

import pytest

from flake8_bas.checker import STATEMENTS, Statement
from .conftest import load_files, parametrized_name, StatementTest


@pytest.mark.parametrize(
    "statement_test", load_files("valid"), indirect=True, ids=parametrized_name
)
def test_valid_statements(statement_test: StatementTest):
    """
    Tests that all files in fixtures/valid/ do not raise any errors.
    """
    assert (
        len(statement_test.checker.tree) > 1
    ), f"{statement_test.file.name} might be empty."

    result = statement_test.run()

    assert len(result) == 0, ", ".join(
        f"{statement_test.file.name}:{e.lineno}:{e.col_offset}" for e in result
    )


@pytest.mark.parametrize(
    "statement_test", load_files("invalid"), indirect=True, ids=parametrized_name
)
def test_invalid_statements(statement_test: StatementTest):
    """
    Tests that all files in fixtures/invalid/:

    1. Raise the number of errors defined in each file name.
    2. All the errors raised are only for errors of the given statement.
    3. All the errors mention only keyword of the given statement.
    4. Raise at least one error for each of the error codes a statement might have.
    """
    result = statement_test.run()

    assert len(result) == statement_test.error_count, (
        f"{statement_test.file.name}: {len(result)} errors detected while "
        f"{statement_test.error_count} errors were expected."
    )

    for item in result:
        error_codes = "|".join(statement_test.statement.errors.astuple())

        assert re.match(f"({error_codes}) ", item.message), (
            f"Error code \"{re.match('([^ ]+)', item.message).groups()[0]}\" "
            f"detected while "
            f"\"{' or '.join(statement_test.statement.errors.astuple())}\" "
            f"were expected."
        )

        assert f'"{statement_test.statement.keyword}"' in item.message

    for error_code in statement_test.statement.errors.astuple():
        assert (
            0
            < len([1 for r in result if re.match(f"{error_code} ", r.message)])
            < len(result)
        ), f"Number of {error_code} errors is supposed to be >0 and <{len(result)}."


def test_overlapping_errors(checker: Callable):
    """
    Tests that two consecutive statements result in overlapping errors, that is
    that both errors point to the same line of code.
    """
    result = list(
        checker(Path(__file__).parent / "fixtures/overlapping_errors.py").run()
    )

    assert len(result) == 2
    assert result[0].lineno == result[1].lineno


def test_error_uniqueness():
    """
    Tests that all statements' error codes and keywords are unique.
    """
    assert (len(set(e for s in STATEMENTS for e in s.errors.astuple()))) == len(
        STATEMENTS
    ) * len(STATEMENTS[0].errors), "Non-unique error code detected."

    assert (len(set(s.keyword for s in STATEMENTS))) == len(
        STATEMENTS
    ), "Non-unique statement keyword detected."


@pytest.mark.parametrize("statement", STATEMENTS, ids=parametrized_name)
def test_error_sequences(statement: Statement):
    """
    Tests that each error has the same last 2 digits but all the first ones differ.
    """
    errors = statement.errors.astuple()

    assert len(set(e[3] for e in errors)) == len(errors)
    assert len(set(e[4:] for e in errors)) == 1

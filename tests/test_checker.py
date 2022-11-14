import re

import pytest

from flake8_bbs.checker import STATEMENTS
from .conftest import load_files


@pytest.mark.parametrize("statement_test", load_files("valid"), indirect=True)
def test_valid_statements(statement_test):
    result = list(statement_test.checker.run())

    assert len(result) == 0, ", ".join(
        f"{statement_test.file.name}:{e.lineno}:{e.col_offset}" for e in result
    )


@pytest.mark.parametrize("statement_test", load_files("invalid"), indirect=True)
def test_invalid_statements(statement_test):
    result = list(statement_test.checker.run())

    assert len(result) == statement_test.error_count, (
        f"{statement_test.file.name}: {len(result)} errors detected while "
        f"{statement_test.error_count} errors were expected"
    )

    # All the error messages should be only for the given error codes
    for item in result:
        error_codes = "|".join(statement_test.error_codes)

        assert re.match(f"({error_codes}) ", item.message), (
            f"Error code \"{re.match('([^ ]+)', item.message).groups()[0]}\" "
            f"detected while \"{' or '.join(statement_test.error_codes)}\" "
            f"were expected"
        )

    # At least one but not all the errors should be for each of the error codes
    for error_code in statement_test.error_codes:
        assert (
            0
            < len([1 for r in result if re.match(f"{error_code} ", r.message)])
            < len(result)
        ), f"Number of {error_code} errors is supposed to be >0 and <{len(result)}"


def test_error_uniqueness():
    assert (
        len(set(e for s in STATEMENTS for e in [s.error_code, s.sibling_error_code]))
    ) == len(STATEMENTS) * 2, "Non-unique error code detected"

    assert (len(set(s.keyword for s in STATEMENTS))) == len(
        STATEMENTS
    ), "Non-unique statement keyword detected"

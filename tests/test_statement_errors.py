import pytest

from flake8_bas.checker import STATEMENTS, Statement
from .conftest import parametrized_name


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

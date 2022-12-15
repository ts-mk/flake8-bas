import ast

import pytest

from flake8_bas.checker import STATEMENTS, Statement, StatementErrorCodes
from .conftest import parametrized_name


class TestStatementSet:
    def test_error_uniqueness(self):
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
    def test_error_sequences(self, statement: Statement):
        """
        Tests that each error has the same last 2 digits but all the first ones differ.
        """
        errors = statement.errors.astuple()

        assert len(set(e[3] for e in errors)) == len(errors)
        assert len(set(e[4:] for e in errors)) == 1


class TestStatementErrorCodes:
    def test_astuple(self):
        assert isinstance(StatementErrorCodes(1, 2, 3).astuple(), tuple)


class TestStatement:
    @pytest.mark.parametrize("error_type", ("before", "after", "sibling"))
    def test_error_message(self, error_type):
        keyword = "abc"
        error_code = 123
        error_codes = {"before": 0, "after": 0, "sibling": 0}
        error_codes[error_type] = error_code
        statement = Statement(
            keyword, ast.Pass, StatementErrorCodes(*error_codes.values()), (1, 1)
        )
        message = statement.error_message(error_type)

        assert isinstance(message, str)
        assert message.startswith(f"{StatementErrorCodes.NAMESPACE}{error_code} ")
        assert keyword in message

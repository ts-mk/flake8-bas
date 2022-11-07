from unittest.mock import patch

import pytest

from flake8_bbs import StatementChecker


def test_valid_statements(valid, error_formatter):
    result = list(valid.checker.run())

    assert len(result) == 0, error_formatter(file=valid.file, errors=result)

    for item in result:
        assert item.message.startswith(f"{valid.error_code} ")


def test_invalid_statements(invalid, error_formatter):
    result = list(invalid.checker.run())

    assert (
        len(result) == invalid.error_count
    ), f"{invalid.file.name}: {invalid.error_count} errors expected"


def test_error_code_uniqueness():
    assert len(set(s.error_code for s in StatementChecker.STATEMENTS)) == len(
        StatementChecker.STATEMENTS
    )


@pytest.mark.parametrize(
    "content, expected",
    (("if 1 == 1:\n    pass", 0), ("a = 1\nif 1 == 1:\n    pass", 1)),
)
def test_stdin(content, expected):
    with patch("flake8_bbs.checker.stdin_get_value", return_value=content):
        result = list(StatementChecker(filename="stdin").run())

        assert len(result) == expected

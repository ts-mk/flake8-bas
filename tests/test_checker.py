import pytest

from flake8_bas.checker import StatementChecker


@pytest.mark.parametrize(
    "value, expected",
    (
        ("\n", True),
        (" \n", True),
        ("\t\n", True),
        (" # \n", False),
    ),
)
def test_blank_line_regex(value, expected):
    assert (StatementChecker.BLANK_LINE_RE.match(value) is not None) is expected

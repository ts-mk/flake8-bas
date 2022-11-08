import re

from flake8_bbs.checker import STATEMENTS


def test_valid_statements(valid, error_formatter):
    result = list(valid.checker.run())

    assert len(result) == 0, error_formatter(file=valid.file, errors=result)


def test_invalid_statements(invalid, error_formatter):
    result = list(invalid.checker.run())

    assert (
        len(result) == invalid.error_count
    ), f"{invalid.file.name}: {invalid.error_count} errors expected"

    for item in result:
        error_codes = "|".join(invalid.error_codes)
        assert re.match(f"({error_codes}) ", item.message)


def test_error_code_uniqueness():
    assert (
        len(
            set(
                [s.error_code for s in STATEMENTS]
                + [s.sibling_error_code for s in STATEMENTS]
            )
        )
    ) == len(STATEMENTS) * 2

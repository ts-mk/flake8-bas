import re

from flake8_bbs.checker import STATEMENTS


def test_valid_statements(valid):
    result = list(valid.checker.run())

    assert len(result) == 0, ", ".join(
        f"{valid.file.name}:{e.lineno}:{e.col_offset}" for e in result
    )


def test_invalid_statements(invalid):
    result = list(invalid.checker.run())

    assert len(result) == invalid.error_count, (
        f"{invalid.file.name}: {len(result)} errors detected while "
        f"{invalid.error_count} errors were expected"
    )

    # All the error messages should be only for the given error codes
    for item in result:
        error_codes = "|".join(invalid.error_codes)

        assert re.match(f"({error_codes}) ", item.message), (
            f"Error code \"{re.match('([^ ]+)', item.message).groups()[0]}\" "
            f"detected while \"{' or '.join(invalid.error_codes)}\" were expected"
        )

    # At least one but not all the errors should be for each of the error codes
    for error_code in invalid.error_codes:
        assert (
            0
            < len([1 for r in result if re.match(f"{error_code} ", r.message)])
            < len(result)
        )


def test_error_code_uniqueness():
    assert (
        len(
            set(
                [s.error_code for s in STATEMENTS]
                + [s.sibling_error_code for s in STATEMENTS]
            )
        )
    ) == len(STATEMENTS) * 2

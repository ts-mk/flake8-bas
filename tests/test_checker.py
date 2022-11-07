from flake8_bbs import StatementChecker


def test_valid_statements(valid, error_compiler):
    result = list(valid.checker.run())

    assert len(result) == 0, error_compiler(file=valid.file, errors=result)

    for item in result:
        assert item.message.startswith(f"{valid.error_code} ")


def test_invalid_statements(invalid, error_compiler):
    result = list(invalid.checker.run())

    assert (
        len(result) == invalid.error_count
    ), f"{invalid.file.name}: {invalid.error_count} errors expected"


def test_error_code_uniqueness():
    assert len(set(s.error_code for s in StatementChecker.STATEMENTS)) == len(
        StatementChecker.STATEMENTS
    )

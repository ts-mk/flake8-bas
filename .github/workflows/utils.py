#!/usr/bin/env python3

import re
import sys
from pathlib import Path
from typing import Optional

from click import (
    Argument,
    CommandCollection,
    Context,
    argument,
    get_text_stream,
    group,
    option,
)


@group()
def main() -> None:
    pass


def stdin(ctx: Context, param: Argument, value: Optional[str] = None) -> Optional[str]:
    """
    Tries to read value from stdin.

    :param ctx: context
    :param param: argument object
    :param value: value, if exists
    :return: value
    """
    if not value and not get_text_stream("stdin").isatty():
        return get_text_stream("stdin").read().strip()
    else:
        return value


@main.command(
    short_help="Asserts that errors reported by Flake8 match expected error count."
)
@argument("errors", callback=stdin, required=False)
@option("--directory", required=True, help="Directory path")
def assert_error_count(errors: str, directory: str) -> None:
    errors = errors or ""
    directory = Path(directory)
    input_error_count = len(errors.split("\n"))
    error_count = 0

    if not directory.is_dir():
        raise Exception("Directory expected")

    for file in directory.rglob("*.py"):
        if not (match := re.match(r"([a-z\s]+)\-(\d+)", file.stem)):
            raise Exception(f"Invalid file name format for {file.name}")

        error_count += int(match.groups()[1])

    if input_error_count != error_count:
        raise Exception(
            f"Invalid error count - {error_count} expected "
            f"but {input_error_count} received"
        )


if __name__ == "__main__":
    try:
        CommandCollection(sources=[main])()
    except Exception as e:
        sys.exit(f"ERROR: {str(e)}")

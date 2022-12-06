#!/usr/bin/env python3

import os
import re
import sys
from pathlib import Path
from random import SystemRandom
from string import ascii_uppercase
from typing import Optional, Union
from xml.etree import ElementTree

from click import Argument, Context, argument, get_text_stream, group, option


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


def save_output(name: str, value: Union[str, int, float]) -> None:
    """
    Creates a new named output that could be used in other workflow steps.

    :param name: name/ID of the output
    :param value: value
    """
    value = str(value)

    try:
        delimiter = "".join(SystemRandom().choice(ascii_uppercase) for _ in range(10))
    except Exception:
        delimiter = "EOF"

    with Path(os.getenv("GITHUB_OUTPUT")).open(mode="a") as f:
        if "\n" in value:
            f.write(f"{name}<<{delimiter}\n{value.strip()}\n{delimiter}\n")
        else:
            f.write(f"{name}={value.strip()}\n")


def add_summary(text: str) -> None:
    """
    Adds text to the job's summary.

    :param text: Markdown content
    """
    with Path(os.getenv("GITHUB_STEP_SUMMARY")).open(mode="a") as f:
        f.write(f"{text}\n\n")


@main.command(
    short_help="Asserts that errors reported by Flake8 match expected error count."
)
@argument("errors", callback=stdin, required=False)
@option("--directory", required=True, help="Directory path")
@option("--exclude", required=False, help="Exclude pattern")
def assert_error_count(
    errors: str, directory: str, exclude: Optional[str] = None
) -> None:
    errors = errors or ""
    directory = Path(directory)
    input_error_count = len(errors.split("\n"))
    error_count = 0

    if not directory.is_dir():
        raise Exception("Directory expected")

    for file in directory.rglob("*.py"):
        if exclude and re.search(exclude, str(file)):
            continue

        if not (match := re.match(r"([a-z_]+)\-(\d+)", file.stem)):
            raise Exception(f"Invalid file name format for {file.name}")

        error_count += int(match.groups()[1])

    if input_error_count != error_count:
        raise Exception(
            f"Invalid error count - {error_count} expected "
            f"but {input_error_count} received"
        )


@main.command(short_help="Outputs coverage result as job's summary.")
@option("--coverage_file", required=True, help="Coverage result file path")
def coverage_summary(coverage_file: str) -> None:
    coverage = round(
        float(ElementTree.parse(coverage_file).getroot().attrib["line-rate"]) * 100
    )

    add_summary(f"**Coverage result:** {coverage}%")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(f"ERROR: {str(e)}")

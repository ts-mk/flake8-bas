#!/usr/bin/env python3

import os
import re
import sys
from datetime import datetime
from pathlib import Path
from random import SystemRandom
from string import ascii_uppercase
from typing import Optional, Union
from xml.etree import ElementTree

from click import Argument, Context, argument, get_text_stream, group, option

# Temp directory and files in it are used only when running this script locally
TEMP = Path(__file__).parents[2] / "tmp"
TEMP.mkdir(exist_ok=True)
(TEMP / "GITHUB_OUTPUT.txt").unlink(missing_ok=True)
(TEMP / "GITHUB_STEP_SUMMARY.txt").unlink(missing_ok=True)

CHANGELOG = Path(__file__).parents[2] / "CHANGELOG.md"
GITHUB_ACTIONS = {"true": True, "false": False}[
    os.getenv("GITHUB_ACTIONS", "false").lower()
]
GITHUB_OUTPUT = Path(os.getenv("GITHUB_OUTPUT", TEMP / "GITHUB_OUTPUT.txt"))
GITHUB_STEP_SUMMARY = Path(
    os.getenv("GITHUB_STEP_SUMMARY", TEMP / "GITHUB_STEP_SUMMARY.txt")
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

    with GITHUB_OUTPUT.open(mode="a") as f:
        if "\n" in value:
            f.write(f"{name}<<{delimiter}\n{value.strip()}\n{delimiter}\n")
        else:
            f.write(f"{name}={value.strip()}\n")


def add_summary(text: str) -> None:
    """
    Adds text to the job's summary.

    :param text: Markdown content
    """
    with GITHUB_STEP_SUMMARY.open(mode="a") as f:
        f.write(f"{text}\n\n")


def version_notes(version: str) -> str:
    """
    Retrieves release notes from CHANGELOG.md.

    :param version: release version
    """
    content = CHANGELOG.read_text()

    try:
        start = re.search(
            rf"^##\s*\[\s*{version}\s*\].*$", content, re.MULTILINE
        ).span()[1]
        end = re.search(r"^##\s*\[", content[start:], re.MULTILINE)

        if end:
            output = content[start : (start + end.span()[0])].strip()  # noqa: E203
        else:
            output = content[start:].strip()
    except Exception as e:
        raise Exception("Failed to locate release notes.") from e

    return output


@main.command(
    short_help="Asserts that errors reported by Flake8 match expected error count."
)
@argument("errors", callback=stdin, required=False)
@option("--directory", required=True, help="Directory path")
@option("--exclude", required=False, help="Exclude pattern")
def assert_error_count(
    errors: str, directory: str, exclude: Optional[str] = None
) -> None:
    directory = Path(directory)
    input_error_count = len(errors.strip().split("\n")) if errors.strip() else 0
    expected_error_count = 0

    if not directory.is_dir():
        raise Exception("Directory expected")

    for file in directory.rglob("*.py"):
        if exclude and re.search(exclude, str(file)):
            continue

        if not (match := re.match(r"([a-z_]+)-(\d+)", file.stem)):
            raise Exception(f"Invalid file name format for {file.name}")

        expected_error_count += int(match.groups()[1])

    if input_error_count != expected_error_count:
        raise Exception(
            f"Invalid error count - {expected_error_count} expected "
            f"but {input_error_count} received"
        )


@main.command(short_help="Outputs coverage result as job's summary.")
@option("--coverage_file", required=True, help="Coverage result file path")
def coverage_summary(coverage_file: str) -> None:
    coverage = round(
        float(ElementTree.parse(coverage_file).getroot().attrib["line-rate"]) * 100
    )

    add_summary(f"**Coverage:** {coverage}%")


@main.command(short_help="Modifies CHANGELOG.md by creating a new release.")
@option("--version", required=True, help="Version to be set")
def write_changelog_release(version: str) -> None:
    keyword = "## [Unreleased]"
    content = CHANGELOG.read_text()

    if not version:
        raise Exception("Missing package version")

    # If the version already exists in the changelog, do nothing
    if f"## [{version}]" in content:
        print(
            f"Changelog entry for version {version} already exists.",
            f"Skipping modification of {CHANGELOG.name}.",
        )

        return

    if keyword not in content:
        raise Exception(f"{keyword} not found in {CHANGELOG.name}")

    CHANGELOG.write_text(
        content.replace(
            keyword,
            f"{keyword}\n\n## [{version}] - {datetime.utcnow().strftime('%Y-%m-%d')}",
        )
    )


@main.command(short_help="Sets all release information in the step's output.")
@option("--version", required=True, help="Version to be set")
@option("--commit", required=True, help="SHA of the commit")
def set_release_data(version: str, commit: str) -> None:
    save_output("commit", commit)
    save_output("tag", f"v{version}")
    save_output("title", version)
    save_output("notes", version_notes(version))
    add_summary(f"**Version:** {version}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        if GITHUB_ACTIONS:
            sys.exit(f"ERROR: {str(e)}")
        else:
            raise

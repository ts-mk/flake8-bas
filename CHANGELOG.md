# Changelog

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Use of `slots` in data classes.
- Compatibility with Python 3.13 and 3.14.

### Changed
- Type hints using a modern syntax.

### Removed
- Compatibility with Python 3.8 and 3.9.

## [1.0.0] - 2024-02-01
### Added
- Compatibility with Python 3.12.

## [0.2.0] - 2023-04-24
### Changed
- Compatibility with Python and subsequently compatibility with Flake8 version 6.x.x.

## [0.1.2] - 2023-01-26
### Fixed
- Statements within `finally` block would cause false-positive errors.

## [0.1.1] - 2023-01-13
### Fixed
- Wrong order of evaluation of content above nodes causing constant string expressions to result in
  a false-positive error.

## [0.1.0] - 2023-01-01
### Added
- Initial version.

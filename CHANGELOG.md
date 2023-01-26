# Changelog

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

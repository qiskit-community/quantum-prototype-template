# GitHub Actions workflows

This directory contains a number of workflows for use with [GitHub Actions](https://docs.github.com/actions).  They specify what standards should be expected for development of this software, including pull requests.  These workflows are designed to work out of the box for any research software prototype, especially those based on [Qiskit](https://qiskit.org/).

## Styles check (`lint.yml`)

This workflow checks that the code is formatted properly and follows the style guide by installing tox and running the [lint environment](/tests/#lint-environment) (`tox -elint`).

## Latest version tests (`test_latest_versions.yml`)

This workflow installs the latest version of tox and runs [the current repository's tests](/tests/#test-py-environments) under each supported Python version on Linux and under a single Python version on macOS and Windows.  This is the primary testing workflow.  It runs for all code changes and additionally once per day, to ensure tests continue to pass as new versions of dependencies are released.

## Code coverage (`coverage.yml`)

This workflow tests the [coverage environment](/tests/#coverage-environment) on a single version of Python by installing tox and running `tox -ecoverage`.

## Citation preview (`citation.yml`)

This workflow is only triggered when the `CITATION.bib` file is changed.  It ensures that the file contains only ASCII characters ([escaped codes](https://en.wikibooks.org/wiki/LaTeX/Special_Characters#Escaped_codes) are preferred, as then the `bib` file will work even when `inputenc` is not used).  It also compiles a sample LaTeX document which includes the citation in its bibliography and uploads the resulting PDF as an artifact so it can be previewed (e.g., before merging a pull request).

File descriptions for template
==============================

- [.github](../.github) - folder for configuring anything related to GitHub.
  For example how issues and pull requests are looking like or CI processes setup (automatic tests, style checks).
  Currently, we have
    - [issue templates](../.github/ISSUE_TEMPLATE)
    - [pull request template](../.github/PULL_REQUEST_TEMPLATE.md)
    - [continuous integration (CI) workflows](../.github/workflows)
- [.gitignore](../.gitignore) - git-specific file that tells which files to ignore
  when tracking/pushing/commiting code (those files will not be tracked by git)
- [.pylintrc](../.pylintrc) - standard style checks configuration file. Content of file is
  self-explanatory. During automatic style checks CI processes are referring to this file
  to get guidelines.
- [.travis.yml](../.travis.yml) - for internal repositories we use Travis - CI framework.
  This is similar framework to GitHub Actions which are described in [CI workflows](../.github/workflows).
- [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) - one of the standard recommendations for open source repositories, including those on GitHub.
  Name speaks for itself.
- [CONTRIBUTING.md](../CONTRIBUTING.md) - one of the standard recommendations for GitHub repositories.
  Contributing guidelines for developers.
- [ecosystem.json](../ecosystem.json) - Qiskit Ecosystem config file needed for adding the project to the [Qiskit Ecosystem](https://github.com/qiskit-community/ecosystem) and see the project on the Qiskit [website](https://qiskit.org/ecosystem).
- [LICENSE.txt](../LICENSE.txt) - one of the standard requirements for an open source project.
  There are different types of [licenses for software](https://en.wikipedia.org/wiki/Software_license).
  [Most popular open-source licenses](https://opensource.org/licenses).
- [README.md](../README.md) - main readme for repository.
- [docs](../docs) - documentation for repository.
- [pyproject.toml](../pyproject.toml) - file that contains the build system requirments for your python project
- [setup.py](../setup.py) - exists for compatibility with legacy tools.
  This is the main configuration file for all Python projects.
- [tests](../tests) - folder where all project tests are located.
  It is a good practice to cover your project with tests to ensure correctness of implementation.
- [tox.ini](../tox.ini) - configuration file for [tox](https://tox.readthedocs.io/en/latest/) framework that
  aims to automate and standardize testing in Python.
  Eases the packaging, testing and release process of Python software.

<div align="center">
  <h1>fpl - FPL API support</h1>
  <br />
  <br />
  <a href="https://github.com/agent-polyblank/fpl/issues/new?assignees=&labels=bug&template=1-bug-report.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/agent-polyblank/fpl/issues/new?assignees=&labels=enhancement&template=4-feature-request.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/agent-polyblank/fpl/discussions">Ask a Question</a>
</div>

<div align="center">
<br />

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Ruff](https://img.shields.io/badge/ruff-3670A0?style=for-the-badge&logo=ruff&logoColor=d7ff64)
![Pre-commit](https://img.shields.io/badge/pre--commit-3670A0?style=for-the-badge&logo=pre-commit&logoColor=fab040)
![PyTest](https://img.shields.io/badge/pytest-3670A0?style=for-the-badge&logo=pytest&logoColor=0a9edc)
</div>


-----

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Installation](#installation)
- [Hatch Environment:](#hatch-environment)
- [Usage](#usage)
  - [Activating the Environment](#activating-the-environment)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Development](#development)
  - [Installing Dependencies](#installing-dependencies)
  - [Linting \& Formatting](#linting--formatting)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Building the Package](#building-the-package)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Hatch**: [Hatch](https://hatch.pypa.io/latest/) allows for modern project management for Python, including environment management, testing, and packaging.
- **Pre-configured linting and formatting:**: [Ruff](https://docs.astral.sh/ruff/) for blazing fast linting and formatting.
- **Pre-configured test suite**: [PyTest](https://docs.pytest.org/en/8.2.x/) for robust testing.
- **Pre-commit**: [Pre-Commit Hooks](https://pre-commit.com/) for automated code checks.

## Installation

```bash
cd fpl
pip install .
```

## Hatch Environment:

1. Navigate to the project directory:

```bash
cd fpl
hatch env create
```

## Usage

### Activating the Environment

To activate the Hatch environment, run:

```bash
hatch shell
```

### Running the Application

After activating the environment, you can run your application using:

```bash
python -m fpl
```

## Project Structure

The project structure follows a standard layout:

```
fpl
 ┣ .github
 ┃ ┣ ISSUE_TEMPLATE
 ┃ ┃ ┣ 1-bug-report.md
 ┃ ┃ ┣ 2-failing-test.md
 ┃ ┃ ┣ 3-docs-bug.md
 ┃ ┃ ┣ 4-feature-request.md
 ┃ ┃ ┣ 5-enhancement-request.md
 ┃ ┃ ┣ 6-security-report.md
 ┃ ┃ ┣ 7-question-support.md
 ┃ ┃ ┗ config.yml
 ┃ ┣ CODEOWNERS
 ┃ ┣ CODE_OF_CONDUCT.md
 ┃ ┣ CONTRIBUTING.md
 ┃ ┣ FUNDING.yml
 ┃ ┣ ISSUE_TEMPLATE.md
 ┃ ┣ SECURITY.md
 ┃ ┣ SUPPORT.md
 ┃ ┣ config.yml
 ┃ ┣ issue_label_bot.yaml
 ┃ ┣ pull_request_template.md
 ┃ ┗ settings.yml
 ┣ src
 ┃ ┗ fpl
 ┃ ┃ ┣ __about__.py
 ┃ ┃ ┣ __init__.py
 ┃ ┃ ┣ __main__.py
 ┃ ┃ ┗ example.py
 ┣ tests
 ┃ ┣ __init__.py
 ┃ ┗ test.py
 ┣ .gitignore
 ┣ .pre-commit-config.yaml
 ┣ LICENSE.txt
 ┣ README.md
 ┗ pyproject.toml
```

## Development

### Installing Dependencies

To install the project dependencies, activate the Hatch environment and run:

```bash
hatch env install
```

### Linting & Formatting

Run the following command to lint and format code with Ruff:

```bash
hatch fmt
```

## Testing

To run tests using PyTest, execute:

```bash
hatch run test
```

## Deployment

### Building the Package

To build the package, run:

```bash
hatch build
```

## Contributing

Contributions to fpl are welcomed! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Install pre-commit hooks
4. Make your changes.
5. Ensure your changes pass pre-commit and conform to the [Contributing Guidelines](./.github/CONTRIBUTING.md) and [Code of Conduct](./.github/CODE_OF_CONDUCT.md).
6. Submit a pull request with a detailed description of your changes Pull Request template can be found [here](./.github/pull_request_template.md).

## License

fpl is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

<!-- pdoc exclude start -->
<div align="center">
  <h1>FPL Wrapper - A Wrapper for the FPL API</h1>
  <br />
  <br />
  <a href="https://github.com/agent-polyblank/fpl-wrapper/issues/new?assignees=&labels=bug&template=1-bug-report.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/agent-polyblank/fpl-wrapper/issues/new?assignees=&labels=enhancement&template=4-feature-request.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/agent-polyblank/fpl-wrapper/discussions">Ask a Question</a>
</div>

<div align="center">
<br />


[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Ruff](https://img.shields.io/badge/ruff-3670A0?style=for-the-badge&logo=ruff&logoColor=d7ff64)
![Pre-commit](https://img.shields.io/badge/pre--commit-3670A0?style=for-the-badge&logo=pre-commit&logoColor=fab040)
![PyTest](https://img.shields.io/badge/pytest-3670A0?style=for-the-badge&logo=pytest&logoColor=0a9edc)
</div>
<!-- pdoc exclude end -->

-----

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Hatch Environment:](#hatch-environment)
- [Usage](#usage)
  - [Activating the Environment](#activating-the-environment)
  - [Running the Application](#running-the-application)
    - [Command Line](#command-line)
- [Development](#development)
  - [Installing Dependencies](#installing-dependencies)
  - [Linting \& Formatting](#linting--formatting)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Building the Package](#building-the-package)
- [Contributing](#contributing)
- [License](#license)


## Installation

```bash
cd fpl_wrapper
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

You can either run the functionality from the command line or use the package as a library.

#### Command Line

When installed the following commands are available:

* `fpl_get_fixtures` - Fetch the fixture list.
* `fpl_get_league_data` - Fetch data for a league (paginated, for larger leagues you will need to specify the page number).
* `fpl_get_manager_gw_data` - Fetch data for a manager (fpl player)
* `fpl_get_players` - Get player data.
* `fpl_get_player` - Get data for a single player.

Usage:

```bash
fpl_get_fixtures 
(no arguments)

fpl_get_league_data
usage: get_league_data [-h] [--league_id LEAGUE_ID] [--page PAGE]

options:
  -h, --help            show this help message and exit
  --league_id LEAGUE_ID
  --page PAGE

fpl_get_manager_gw_data
usage: get_manager_gw_data [-h] [--team_id TEAM_ID] [--gw GW]

options:
  -h, --help         show this help message and exit
  --team_id TEAM_ID
  --gw GW

fpl_get_players
(no arguments)

fpl_get_player
usage: get_player [-h] [--player_id PLAYER_ID]

options:
  -h, --help            show this help message and exit
  --player_id PLAYER_ID
```

Or alternatively you can use the package as a library:

```python
from fpl_wrapper.data_fetch.fixtures import get_fixtures
get_fixtures()
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

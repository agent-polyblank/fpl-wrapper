<div align="center">
  <h1>FPL Wrapper - A Wrapper for the FPL API</h1>
  <a href="https://github.com/agent-polyblank/fpl-wrapper/issues/new?assignees=&labels=bug&template=1-bug-report.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/agent-polyblank/fpl-wrapper/issues/new?assignees=&labels=enhancement&template=4-feature-request.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/agent-polyblank/fpl-wrapper/discussions">Ask a Question</a>
  <br />
  <br />
  <img src="https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge" alt="Licence">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/ruff-3670A0?style=for-the-badge&logo=ruff&logoColor=d7ff64" alt="Ruff">
  <img src="https://img.shields.io/badge/pre--commit-3670A0?style=for-the-badge&logo=pre-commit&logoColor=fab040" alt="Pre-commit">
  <img src="https://img.shields.io/badge/pytest-3670A0?style=for-the-badge&logo=pytest&logoColor=0a9edc" alt="PyTest">
</div>
<br />

## Table of Contents

- [FPL API Endpoint Support Matrix](#fpl-api-endpoint-support-matrix)
  - [Usage Examples](#usage-examples)
  - [Future Development](#future-development)
  - [Hatch Environment:](#hatch-environment)
  - [Usage](#usage)
    - [Activating the Environment](#activating-the-environment)
    - [Running the Application](#running-the-application)
      - [Command Line](#command-line)
  - [Development](#development)
    - [Installing Dependencies](#installing-dependencies)
    - [Linting \& Formatting](#linting--formatting)
  - [Testing](#testing)
- [Documentation](#documentation)
  - [Deployment](#deployment)
    - [Building the Package](#building-the-package)
  - [Contributing](#contributing)
  - [License](#license)


## FPL API Endpoint Support Matrix

This table provides an overview of the Fantasy Premier League API endpoints supported by the FPL Wrapper library.

| Endpoint                                                        | Status          | Method                  | Description                                                   | CLI Command                                      |
| --------------------------------------------------------------- | --------------- | ----------------------- | ------------------------------------------------------------- | ------------------------------------------------ |
| `/bootstrap-static/`                                            | ✅ Supported     | `get_bootstrap_data()`  | Retrieves static data including teams, players, game settings | N/A (internal use)                               |
| `/fixtures/`                                                    | ✅ Supported     | `get_fixtures()`        | Retrieves all fixtures for the season                         | `fpl_get_fixtures`                               |
| `/element-summary/{player_id}/`                                 | ✅ Supported     | `get_player_by_id()`    | Retrieves detailed data for a specific player                 | `fpl_get_player --player_id ID`                  |
| `/elements/`                                                    | ✅ Supported     | `get_players()`         | Retrieves all player data                                     | `fpl_get_players`                                |
| `/entry/{team_id}/event/{event_id}/picks/`                      | ✅ Supported     | `get_manager_gw_data()` | Retrieves team selection for a specific manager in a gameweek | `fpl_get_manager_gw_data --team_id ID --gw GW`   |
| `/leagues-classic/{league_id}/standings/?page_standings={page}` | ✅ Supported     | `get_league_data()`     | Retrieves standings for a classic league                      | `fpl_get_league_data --league_id ID --page PAGE` |
| `/entry/{team_id}/history/`                                     | ❌ Not Supported | -                       | Retrieves a manager's season history                          | -                                                |
| `/dream-team/`                                                  | ❌ Not Supported | -                       | Retrieves the dream team                                      | -                                                |
| `/entry/{team_id}/`                                             | ❌ Not Supported | -                       | Retrieves general data about an FPL team                      | -                                                |
| `/event/{event_id}/live/`                                       | ❌ Not Supported | -                       | Retrieves live player data for a gameweek                     | -                                                |
| `/event-status/`                                                | ❌ Not Supported | -                       | Retrieves status of each gameweek                             | -                                                |
| `/my-team/{team_id}/`                                           | ❌ Not Supported | -                       | Retrieves authenticated user's team                           | -                                                |
| `/transfers/`                                                   | ❌ Not Supported | -                       | Retrieves authenticated user's transfer data                  | -                                                |
| `/me/`                                                          | ❌ Not Supported | -                       | Retrieves authenticated user data                             | -                                                |

## Future Development

We plan to add support for additional endpoints in future releases. If you need a specific endpoint that's not yet supported, please open an issue or submit a pull request.

## Hatch Environment:

This project uses [Hatch](https://hatch.pypa.io/latest/) for environment management. To set up the environment, follow these steps:
1. Install Hatch if you haven't already:

```bash
uv pip install hatch
```

2. Navigate to the project directory:

```bash
hatch env create
```

## Usage

### Activating the Environment

To activate the Hatch environment, run:

```bash
hatch shell
```

### Running the Application

```
uv pip install .
```
#### Command Line

When installed the following commands are available:

* `fpl_get_fixtures` - Fetch the fixture list for the current season.
* `fpl_get_league_data` - Fetch standings data for a classic league with pagination support.
* `fpl_get_manager_gw_data` - Fetch team selection data for a specific manager in a gameweek.
* `fpl_get_players` - Get detailed data for all players in the game.
* `fpl_get_player` - Get detailed information and history for a specific player.

Usage:

```bash
fpl_get_fixtures 
(no arguments)
# Returns all fixtures for the current FPL season

fpl_get_league_data
usage: get_league_data [-h] [--league_id LEAGUE_ID] [--page PAGE]

options:
  -h, --help            show this help message and exit
  --league_id LEAGUE_ID  The ID of the classic league to retrieve
  --page PAGE           The page number for paginated results (default: 1)

fpl_get_manager_gw_data
usage: get_manager_gw_data [-h] [--team_id TEAM_ID] [--gw GW]

options:
  -h, --help         show this help message and exit
  --team_id TEAM_ID  The FPL team/entry ID for the manager
  --gw GW            The gameweek number to retrieve data for

fpl_get_players
(no arguments)
# Returns data for all players in the current FPL season

fpl_get_player
usage: get_player [-h] [--player_id PLAYER_ID]

options:
  -h, --help            show this help message and exit
  --player_id PLAYER_ID  The ID of the player to retrieve detailed data for
```

There is also functionality to get various resources from the fpl server such as shirt images, player images, and team logos. These can be accessed via the `FPLWrapper` class methods:

```bash
fpl_get_team_shirts
usage: fpl_get_team_shirts [-h] --team_id TEAM_ID [--output_directory OUTPUT_DIRECTORY] [--keeper-shirt]

options:
  -h, --help            show this help message and exit
  --team_id TEAM_ID
  --output_directory OUTPUT_DIRECTORY
  --keeper-shirt

fpl_get_all_team_shirts
usage: fpl_get_all_team_shirts [-h] [--output_directory OUTPUT_DIRECTORY]

options:
  -h, --help            show this help message and exit
  --output_directory OUTPUT_DIRECTORY

usage: fpl_get_team_crest [-h] --team_id TEAM_ID

options:
  -h, --help         show this help message and exit
  --team_id TEAM_ID

usage: fpl_get_all_team_crests [-h] [--output_directory OUTPUT_DIRECTORY]

options:
  -h, --help            show this help message and exit
  --output_directory OUTPUT_DIRECTORY

```

Or alternatively you can use the package as a library:

The documentation can be found [here](TODO)

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
hatch run test:test
```
You can also run tests with coverage:

```bash
hatch run test:cov-xml
```
You can also generate a coverage report in HTML format:

```bash
hatch run test:cov-html
```

# Documentation

The documentation is generated using [pdoc](https://pdoc.dev/) and can be found in the `docs` directory. To generate the documentation, run:

```bash
hatch run docs:build
```


## Deployment

### Building the Package

To build the package, run:

```bash
hatch build
```

## Contributing

Contributions to this project are welcomed! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Install pre-commit hooks
4. Make your changes.
5. Ensure your changes pass pre-commit and conform to the [Contributing Guidelines](./.github/CONTRIBUTING.md) and [Code of Conduct](./.github/CODE_OF_CONDUCT.md).
6. Submit a pull request with a detailed description of your changes Pull Request template can be found [here](./.github/pull_request_template.md).

## License

This project is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

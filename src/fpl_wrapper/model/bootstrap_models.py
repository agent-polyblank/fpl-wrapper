"""Models for bootstrap data."""

from enum import StrEnum
from http import HTTPStatus
from pathlib import Path
from typing import Any

import httpx
from pydantic import BaseModel

from fpl_wrapper.data_fetch.exception import ClubCrestNotFoundError
from fpl_wrapper.model.players_models import PlayerDetail


class TeamData(BaseModel):
    """Team data model."""

    code: int
    draw: int
    form: str | None
    id: int
    loss: int
    name: str
    played: int
    points: int
    position: int
    short_name: str
    strength: int
    team_division: int | None
    unavailable: bool
    win: int
    strength_overall_home: int
    strength_overall_away: int
    strength_attack_home: int
    strength_attack_away: int
    strength_defence_home: int
    strength_defence_away: int
    pulse_id: int

    def get_team_crest(
        self,
        client: httpx.Client,
        output_directory: str = "club_crests/",
    ) -> None:
        """
        Fetch team crest image.

        Args:
        ----
            output_directory (str): Directory to save the image.
            client (httpx.Client): HTTP client instance.

        Args:
        ----
            output_directory (str): _description_
            client (httpx.Client): _description_

        Raises:
        ------
            PhotoNotFoundError: _description_

        """
        filename = f"{self.code}_{self.name}.png"
        output_path = Path(output_directory) / filename
        url = f"https://resources.premierleague.com/premierleague/badges/100/t{self.code}@x2.png"
        if not output_path.parent.exists():
            output_path.parent.mkdir(parents=True, exist_ok=False)

        with output_path.open("wb") as file:
            response = client.get(url)
            if response.status_code != HTTPStatus.OK:
                raise ClubCrestNotFoundError(
                    team_code=self.code,
                    team_name=self.name,
                    reason=f"HTTP {response.status_code}: {response.text}",
                )
            file.write(response.content)


class ChipPlay(BaseModel):
    """Chip play model."""

    chip_name: str
    num_played: int


class TopElementInfo(BaseModel):
    """Top element info model."""

    id: int
    points: int


class EventOverrides(BaseModel):
    """Overrides model."""

    # rules: dict[str, Any]  # noqa: ERA001
    # scoring: dict[str, Any]  # noqa: ERA001
    # element_types: list[Any]  # noqa: ERA001
    pick_multiplier: int | None


class Event(BaseModel):
    """Gameweek model."""

    id: int
    name: str
    deadline_time: str
    release_time: str | None
    average_entry_score: int
    finished: bool
    data_checked: bool
    highest_scoring_entry: int | None
    deadline_time_epoch: int
    deadline_time_game_offset: int
    highest_score: int | None
    is_previous: bool
    is_current: bool
    is_next: bool
    cup_leagues_created: bool
    h2h_ko_matches_created: bool
    can_enter: bool
    can_manage: bool
    released: bool
    ranked_count: int
    overrides: EventOverrides
    chip_plays: list[ChipPlay]
    most_selected: int | None
    most_transferred_in: int | None
    top_element: int | None
    top_element_info: TopElementInfo | None
    transfers_made: int
    most_captained: int | None
    most_vice_captained: int | None


class ElementType(BaseModel):
    """Model for player element type."""

    id: int
    plural_name: str
    plural_name_short: str
    singular_name: str
    singular_name_short: str
    squad_select: int
    squad_min_select: int | None
    squad_max_select: int | None
    squad_min_play: int
    squad_max_play: int
    ui_shirt_specific: bool
    sub_positions_locked: list[int]
    element_count: int


class Overrides(BaseModel):
    """
    Overrides model.

    Note: We dont actually know what rules,scores and pick_multiplier are.
    """

    rules: dict[str, Any]
    scoring: dict[str, Any]
    element_types: list[ElementType]
    pick_multiplier: Any | None


class ChipTypeEnum(StrEnum):
    """Chip type enum."""

    TRANSFER = "transfer"
    TEAM = "team"


class Chip(BaseModel):
    """Chip model."""

    id: int
    name: str
    number: int
    start_event: int
    stop_event: int
    chip_type: ChipTypeEnum
    overrides: Overrides


class GameSettings(BaseModel):
    """Game settings model."""


class GameConfig(BaseModel):
    """Game config model."""


class Phase(BaseModel):
    """Phase model."""

    id: int
    name: str
    start_event: int
    stop_event: int


class ElementStat(BaseModel):
    """Element stat model."""


class BootstrapData(BaseModel):
    """Bootstrap data model."""

    chips: list[Chip]
    events: list[Event]
    game_settings: GameSettings
    game_config: GameConfig
    phases: list[Phase]
    teams: list[TeamData]
    total_players: int
    element_stats: list[ElementStat]
    element_types: list[ElementType]
    elements: list[PlayerDetail]

"""Models for bootstrap data."""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel

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
    highest_scoring_entry: int
    deadline_time_epoch: int
    deadline_time_game_offset: int
    highest_score: int
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
    most_selected: int
    most_transferred_in: int
    top_element: int
    top_element_info: TopElementInfo
    transfers_made: int
    most_captained: int
    most_vice_captained: int


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

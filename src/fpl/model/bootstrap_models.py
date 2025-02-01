"""Models for bootstrap data."""

from pydantic import BaseModel


class TeamData(BaseModel):
    """Team data model."""

    code: int
    draw: int
    form: str
    id: int
    loss: int
    name: str
    played: int
    points: int
    position: int
    short_name: str
    strength: int
    team_division: int
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


class Overrides(BaseModel):
    """Overrides model."""

    # rules: dict[str, Any]  # noqa: ERA001
    # scoring: dict[str, Any]  # noqa: ERA001
    # element_types: list[Any]  # noqa: ERA001
    pick_multiplier: int


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
    overrides: Overrides
    chip_plays: list[ChipPlay]
    most_selected: int
    most_transferred_in: int
    top_element: int
    top_element_info: TopElementInfo
    transfers_made: int
    most_captained: int
    most_vice_captained: int

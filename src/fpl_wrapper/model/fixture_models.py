"""Models for fixtures."""

from enum import StrEnum

from pydantic import BaseModel


class StatIdentifier(StrEnum):
    """Identifiers for stats."""

    GOALS_SCORED = "goals_scored"
    ASSISTS = "assists"
    OWN_GOALS = "own_goals"
    PENALTIES_SAVED = "penalties_saved"
    PENALTIES_MISSED = "penalties_missed"
    YELLOW_CARDS = "yellow_cards"
    RED_CARDS = "red_cards"
    SAVES = "saves"
    BONUS = "bonus"
    BPS = "bps"
    MNG_UNDERDOG_WIN = "mng_underdog_win"
    MNG_UNDERDOG_DRAW = "mng_underdog_draw"


class StatElement(BaseModel):
    """Stat element."""

    value: int
    element: int


class Stat(BaseModel):
    """Stat model."""

    identifier: StatIdentifier
    a: list[StatElement]
    h: list[StatElement]


class Fixture(BaseModel):
    """Match data model."""

    code: int
    event: int
    finished: bool
    finished_provisional: bool | None
    id: int
    kickoff_time: str
    minutes: int
    provisional_start_time: bool
    started: bool | None
    team_a: int
    team_a_score: int | None
    team_h: int
    team_h_score: int | None
    stats: list[Stat] | None
    team_h_difficulty: int | None
    team_a_difficulty: int | None
    pulse_id: int | None


class Fixtures(BaseModel):
    """Fixtures model."""

    fixtures: list[Fixture]

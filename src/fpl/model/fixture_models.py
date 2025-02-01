"""Models for fixtures."""

from enum import Enum

from pydantic import BaseModel


class StatIdentifier(str, Enum):
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


class MatchData(BaseModel):
    """Match data model."""

    code: int
    event: int
    finished: bool
    finished_provisional: bool
    id: int
    kickoff_time: str
    minutes: int
    provisional_start_time: bool
    started: bool
    team_a: int
    team_a_score: int
    team_h: int
    team_h_score: int
    stats: list[Stat]
    team_h_difficulty: int
    team_a_difficulty: int
    pulse_id: int

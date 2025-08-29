"""Models for Gameweek live data."""

from pydantic import BaseModel


class LiveExplainStat(BaseModel):
    """Per-stat explanation for a fixture."""

    identifier: str
    points: int
    value: int
    points_modification: int | None = 0


class LiveExplainItem(BaseModel):
    """Fixture breakdown explaining how points were earned."""

    fixture: int
    stats: list[LiveExplainStat]


class LiveElementStats(BaseModel):
    """Aggregated live stats for a player in an event."""

    minutes: int
    goals_scored: int
    assists: int
    clean_sheets: int
    goals_conceded: int
    own_goals: int
    penalties_saved: int
    penalties_missed: int
    yellow_cards: int
    red_cards: int
    saves: int
    bonus: int
    bps: int
    influence: str
    creativity: str
    threat: str
    ict_index: str
    clearances_blocks_interceptions: int
    recoveries: int
    tackles: int
    defensive_contribution: int
    starts: int
    expected_goals: str
    expected_assists: str
    expected_goal_involvements: str
    expected_goals_conceded: str
    total_points: int
    in_dreamteam: bool


class LiveElement(BaseModel):
    """Live element item within an event."""

    id: int
    stats: LiveElementStats
    explain: list[LiveExplainItem]
    modified: bool


class EventLiveResponse(BaseModel):
    """Top-level response for event live endpoint."""

    elements: list[LiveElement]

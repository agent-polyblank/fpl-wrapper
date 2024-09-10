"""Models for the FPL API."""

from pydantic import BaseModel


class Fixture(BaseModel):
    """Fixture model."""

    id: int
    code: int
    team_h: int
    team_h_score: int | None
    team_a: int
    team_a_score: int | None
    event: int
    finished: bool
    minutes: int
    provisional_start_time: bool
    kickoff_time: str
    event_name: str
    is_home: bool
    difficulty: int


class History(BaseModel):
    """History model."""

    element: int
    fixture: int
    opponent_team: int
    total_points: int
    was_home: bool
    kickoff_time: str
    team_h_score: int
    team_a_score: int
    round: int
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
    starts: int
    expected_goals: str
    expected_assists: str
    expected_goal_involvements: str
    expected_goals_conceded: str
    value: int
    transfers_balance: int
    selected: int
    transfers_in: int
    transfers_out: int


class HistoryPast(BaseModel):
    """History past model."""

    season_name: str
    element_code: int
    start_cost: int
    end_cost: int
    total_points: int
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
    starts: int
    expected_goals: str
    expected_assists: str
    expected_goal_involvements: str
    expected_goals_conceded: str


class PlayerData(BaseModel):
    """Player data model."""

    fixtures: list[Fixture]
    history: list[History]
    history_past: list[HistoryPast]

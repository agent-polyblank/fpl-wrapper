"""Models for player data."""

from enum import IntEnum

from pydantic import BaseModel, Field


class PositionEnum(IntEnum):
    """Enum for player positions."""

    Goalkeeper = 1
    Defender = 2
    Midfielder = 3
    Forward = 4
    Manager = 5

    def __str__(self) -> str:
        """Get string representation."""
        return self.name.capitalize()


class Fixture(BaseModel):
    """Fixture model."""

    id: int
    code: int
    team_h: int
    team_h_score: int | None
    team_a: int
    team_a_score: int | None
    event: int | None
    finished: bool
    minutes: int
    provisional_start_time: bool
    kickoff_time: str | None
    event_name: str | None = None
    is_home: bool
    difficulty: int


class Club(BaseModel):
    """Team model."""

    code: int
    draw: int
    form: int | None
    id: int
    loss: int
    name: str
    played: int
    points: int
    position: int
    short_name: str
    strength: int
    team_division: str | None
    unavailable: bool
    win: int
    strength_overall_home: int
    strength_overall_away: int
    strength_attack_home: int
    strength_attack_away: int
    strength_defence_home: int
    strength_defence_away: int
    pulse_id: int


class History(BaseModel):
    """History model."""

    element: int
    fixture: int
    opponent_team: int
    total_points: int
    was_home: bool
    kickoff_time: str
    team_h_score: int | None
    team_a_score: int | None
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


class PlayerDetail(BaseModel):
    """Details from player bootstrap-static endpoint."""

    chance_of_playing_next_round: int | None
    chance_of_playing_this_round: int | None
    code: int
    cost_change_event: int
    cost_change_event_fall: int
    cost_change_start: int
    cost_change_start_fall: int
    dreamteam_count: int
    element_type: int  # Integer representation of position
    ep_next: str
    ep_this: str
    event_points: int
    first_name: str
    form: str
    id: int
    in_dreamteam: bool
    news: str
    news_added: str | None
    now_cost: int
    photo: str
    points_per_game: str
    second_name: str
    selected_by_percent: str
    special: bool
    squad_number: int | None
    status: str
    team: int
    team_code: int
    total_points: int
    transfers_in: int
    transfers_in_event: int
    transfers_out: int
    transfers_out_event: int
    value_form: str
    value_season: str
    web_name: str
    region: int | None
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
    influence_rank: int
    influence_rank_type: int
    creativity_rank: int
    creativity_rank_type: int
    threat_rank: int
    threat_rank_type: int
    ict_index_rank: int
    ict_index_rank_type: int
    corners_and_indirect_freekicks_order: int | None
    corners_and_indirect_freekicks_text: str | None
    direct_freekicks_order: int | None
    direct_freekicks_text: str | None
    penalties_order: int | None
    penalties_text: str | None
    expected_goals_per_90: float
    saves_per_90: float
    expected_assists_per_90: float
    expected_goal_involvements_per_90: float
    expected_goals_conceded_per_90: float
    goals_conceded_per_90: float
    now_cost_rank: int
    now_cost_rank_type: int
    form_rank: int
    form_rank_type: int
    points_per_game_rank: int
    points_per_game_rank_type: int
    selected_rank: int
    selected_rank_type: int
    starts_per_90: float
    clean_sheets_per_90: float

    # A property to store the player's position based on element_type
    position: str = Field(default="Unknown", init=False)

    def model_post_init(self, __context) -> None:  # noqa: ANN001
        """Set the player's position based on element_type."""
        self.position = PositionEnum(self.element_type).name


class PlayerData(BaseModel):
    """Player data model."""

    player_detail: PlayerDetail = None
    fixtures: list[Fixture]
    history: list[History]
    history_past: list[HistoryPast]

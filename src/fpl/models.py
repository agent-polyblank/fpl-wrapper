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


class PlayerDetail(BaseModel):
    """Details from player bootstrap-static endpoint."""

    chance_of_playing_next_round: int
    chance_of_playing_this_round: int
    code: int
    cost_change_event: int
    cost_change_event_fall: int
    cost_change_start: int
    cost_change_start_fall: int
    dreamteam_count: int
    element_type: int
    ep_next: str
    ep_this: str
    event_points: int
    first_name: str
    form: str
    id: int
    in_dreamteam: bool
    news: str
    news_added: str
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
    region: str | None
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

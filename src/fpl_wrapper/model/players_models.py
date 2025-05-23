"""Models for player data in FPL API."""

from enum import Enum
from http import HTTPStatus
from pathlib import Path

import httpx
from pydantic import BaseModel, ConfigDict

from fpl_wrapper.data_fetch.exception import PhotoNotFoundError

BASE_PHOTO_URL = (
    "https://resources.premierleague.com/premierleague/photos/players/250x250"
)


class PlayerTypesEnum(int, Enum):
    """Enum for player types."""

    GOALKEEPER = 1
    DEFENDER = 2
    MIDFIELDER = 3
    FORWARD = 4
    MANAGER = 5


class PlayerFixture(BaseModel):
    """Model for player fixture data."""

    id: int
    code: int
    team_h: int
    team_a: int
    event: int = None
    finished: bool = None
    minutes: int | None = None
    provisional_start_time: bool = None
    kickoff_time: str | None = None
    event_name: str | None = None
    is_home: bool
    difficulty: int
    finished_provisional: bool | None = None
    started: bool | None = None
    stats: list | None = None
    team_h_difficulty: int | None = None
    team_a_difficulty: int | None = None
    pulse_id: int | None = None


class PlayerHistory(BaseModel):
    """Model for player history data."""

    element: int
    fixture: int
    opponent_team: int
    total_points: int
    was_home: bool
    kickoff_time: str | None = None
    team_h_score: int | None = None
    team_a_score: int | None = None
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
    value: int
    transfers_balance: int
    selected: int
    transfers_in: int
    transfers_out: int

    model_config = ConfigDict(extra="ignore")


class PlayerHistoryPast(BaseModel):
    """Model for player history past seasons."""

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


class PlayerSummaryResponse(BaseModel):
    """Model for player summary response."""

    fixtures: list[PlayerFixture]
    history: list[PlayerHistory]
    history_past: list[PlayerHistoryPast]


class PlayerDetail(BaseModel):
    """Model for player detail."""

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

    region: int | None = None
    team_join_date: str | None = None
    birth_date: str | None = None
    has_temporary_code: bool = False
    opta_code: str | None = None

    def get_player_photo(self, output_directory: str = "/player_photos") -> str:
        """
        Download player photo.

        Args:
        ----
            output_directory (str): Directory to save the photo.

        Returns:
        -------
            str: Player photo URL.

        """
        client = httpx.Client()

        if self.element_type == PlayerTypesEnum.MANAGER:  # Manager
            url = f"{BASE_PHOTO_URL}/{self.opta_code}.png"
        else:
            url = f"{BASE_PHOTO_URL}/p{self.code}.png"

        filename = f"{self.code}_{self.web_name}.png"
        output_path = Path(output_directory) / filename

        if not output_path.parent.exists():
            output_path.parent.mkdir(parents=True, exist_ok=False)

        with output_path.open("wb") as file:
            response = client.get(url)
            if response.status_code != HTTPStatus.OK:
                raise PhotoNotFoundError(
                    image=filename,
                    reason=f"HTTP {response.status_code}: {response.text}",
                )
            file.write(response.content)


class PlayerData(BaseModel):
    """Model for player data."""

    player_detail: PlayerDetail
    fixtures: list[PlayerFixture]
    history: list[PlayerHistory]
    history_past: list[PlayerHistoryPast]

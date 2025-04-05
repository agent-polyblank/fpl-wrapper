"""Pydantic models for the manager basic data."""

from pydantic import BaseModel


class ActivePhase(BaseModel):
    """Model for active phase."""

    phase: int
    rank: int
    last_rank: int
    rank_sort: int
    total: int
    league_id: int
    rank_count: int
    entry_percentile_rank: int


class ClassicLeague(BaseModel):
    """Model for classic league."""

    id: int
    name: str
    short_name: str | None
    created: str
    closed: bool
    rank: int | None
    max_entries: int | None
    league_type: str
    scoring: str
    admin_entry: int | None
    start_event: int
    entry_can_leave: bool
    entry_can_admin: bool
    entry_can_invite: bool
    has_cup: bool
    cup_league: int | None
    cup_qualified: bool | None
    rank_count: int
    entry_percentile_rank: int
    active_phases: list[ActivePhase]
    entry_rank: int
    entry_last_rank: int


class H2HLeague(BaseModel):
    """Model for head to head league."""

    id: int
    name: str
    short_name: str | None
    created: str
    closed: bool
    rank: int | None
    max_entries: int | None
    league_type: str
    scoring: str
    admin_entry: int
    start_event: int
    entry_can_leave: bool
    entry_can_admin: bool
    entry_can_invite: bool
    has_cup: bool
    cup_league: int | None
    cup_qualified: bool | None
    rank_count: int | None
    entry_percentile_rank: int | None
    active_phases: list[ActivePhase]
    entry_rank: int
    entry_last_rank: int


class CupMatch(BaseModel):
    """Model for cup match."""

    id: int
    entry_1_entry: int
    entry_1_name: str
    entry_1_player_name: str
    entry_1_points: int
    entry_1_win: int
    entry_1_draw: int
    entry_1_loss: int
    entry_1_total: int
    entry_2_entry: int
    entry_2_name: str
    entry_2_player_name: str
    entry_2_points: int
    entry_2_win: int
    entry_2_draw: int
    entry_2_loss: int
    entry_2_total: int
    is_knockout: bool
    league: int
    winner: int
    seed_value: int | None
    event: int
    tiebreak: str | None
    is_bye: bool
    knockout_name: str


class CupStatus(BaseModel):
    """Model for cup status."""

    qualification_event: int | None
    qualification_numbers: int | None
    qualification_rank: int | None
    qualification_state: str | None


class Cup(BaseModel):
    """Model for cup."""

    matches: list[CupMatch]
    status: CupStatus
    cup_league: int | None


class Leagues(BaseModel):
    """Model for leagues."""

    classic: list[ClassicLeague] | None
    h2h: list[H2HLeague] | None
    cup: Cup | None
    cup_matches: list[CupMatch] | None


class ManagerBase(BaseModel):
    """Model for player."""

    id: int
    joined_time: str
    started_event: int
    favourite_team: int
    player_first_name: str
    player_last_name: str
    player_region_id: int
    player_region_name: str
    player_region_iso_code_short: str
    player_region_iso_code_long: str
    years_active: int
    summary_overall_points: int
    summary_overall_rank: int
    summary_event_points: int
    summary_event_rank: int
    current_event: int
    leagues: Leagues
    name: str
    name_change_blocked: bool
    entered_events: list[int]
    kit: str
    last_deadline_bank: int
    last_deadline_value: int
    last_deadline_total_transfers: int

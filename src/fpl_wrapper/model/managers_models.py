"""Models for the FPL API."""

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel

from fpl_wrapper.model.players_models import PlayerData


class NewEntry(BaseModel):
    """New entry model."""

    has_next: bool
    page: int
    results: list[dict]


class League(BaseModel):
    """League model."""

    id: int
    name: str
    created: datetime
    closed: bool
    max_entries: int | None
    league_type: str
    scoring: str
    admin_entry: int | None
    start_event: int
    code_privacy: str
    has_cup: bool
    cup_league: int | None
    rank: int | None


class Manager(BaseModel):
    """Manager model."""

    id: int
    event_total: int
    player_name: str
    rank: int
    last_rank: int
    rank_sort: int
    total: int
    entry: int
    entry_name: str


class Standings(BaseModel):
    """Standings model."""

    has_next: bool
    page: int
    results: list[Manager]


class LeagueData(BaseModel):
    """League data model."""

    new_entries: NewEntry
    last_updated_data: datetime
    league: League
    standings: Standings


class EntryHistory(BaseModel):
    """Model for manager entry history."""

    event: int
    points: int
    total_points: int
    rank: int
    rank_sort: int
    overall_rank: int
    percentile_rank: int
    bank: int
    value: int
    event_transfers: int
    event_transfers_cost: int
    points_on_bench: int


class Pick(BaseModel):
    """Model for manager picks."""

    element: int
    position: int
    multiplier: int
    is_captain: bool
    is_vice_captain: bool


class Formation(BaseModel):
    """Model for formation."""

    attackers: int
    midfielders: int
    defenders: int
    goalkeepers: int = 1

    def __str__(self) -> str:
        """Get string representation."""
        return f"{self.attackers}-{self.midfielders}-{self.defenders}-{self.goalkeepers}"  # noqa: E501

    def __hash__(self) -> int:
        """Hash based on attributes."""
        return hash(
            (self.attackers, self.midfielders, self.defenders, self.goalkeepers)
        )


class ChipsEnum(StrEnum):
    """Enum for chips."""

    bench_boost = "bboost"
    free_hit = "freehit"
    triple_captain = "3xc"
    wildcard = "wildcard"


class ManagerTeamData(BaseModel):
    """Model for team data."""

    active_chip: ChipsEnum | None
    automatic_subs: list[dict]
    entry_history: EntryHistory
    picks: list[Pick]


class PlayerTeam(BaseModel):
    """Player team model."""

    goalkeepers: list[PlayerData] = []
    defenders: list[PlayerData] = []
    midfielders: list[PlayerData] = []
    forwards: list[PlayerData] = []

    def __str__(self) -> str:
        """Str representation."""
        str_output = ""
        count = 1
        for i, goalkeeper in enumerate(self.goalkeepers):
            str_output += (
                f"{count + i} : {goalkeeper.player_detail.web_name} \n"
            )
        count += len(self.goalkeepers)

        for i, midfielder in enumerate(self.defenders):
            str_output += (
                f"{count + i} : {midfielder.player_detail.web_name} \n"
            )

        count += len(self.defenders)

        for i, midfielder in enumerate(self.midfielders):
            str_output += (
                f"{count + i} : {midfielder.player_detail.web_name} \n"
            )

        count += len(self.midfielders)

        for i, forward in enumerate(self.forwards):
            str_output += f"{count + i} : {forward.player_detail.web_name} \n"
        return str_output

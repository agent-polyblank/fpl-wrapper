"""Model For dream team."""

from pydantic import BaseModel


class TopPlayer(BaseModel):
    """Model for the top performing player."""

    id: int
    points: int


class TeamPlayer(BaseModel):
    """Model for each player in the team."""

    element: int
    points: int
    position: int


class DreamTeam(BaseModel):
    """Dream team model containing top player and full team."""

    top_player: TopPlayer
    team: list[TeamPlayer]

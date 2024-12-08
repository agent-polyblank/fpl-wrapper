"""Data analysis model for Fantasy Premier League data analysis."""

from typing import TypedDict

from pydantic import BaseModel


class PlayerCount(TypedDict):
    """Player count data analysis model."""

    player_id: int
    player_count: int


class GameweekRange(BaseModel):
    """Class for a gameweek range."""

    gameweek_from: int
    gameweek_to: int

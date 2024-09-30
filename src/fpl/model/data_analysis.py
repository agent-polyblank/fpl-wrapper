"""Data analysis model for Fantasy Premier League data analysis."""

from typing import TypedDict


class PlayerCount(TypedDict):
    """Player count data analysis model."""

    player_id: int
    player_count: int

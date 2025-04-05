"""Functions to fetch team data from the FPL API."""

from fpl_wrapper.model.club_models import Club


def get_teams(data: dict[str, any]) -> list[Club]:
    """
    Get team data from the FPL API.

    Args:
    ----
        data (dict[str, any]): league data.

    Returns:
    -------
        list[Team]: list of teams.

    """
    return [Club(**team) for team in data["teams"]]

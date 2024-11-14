"""Logic for parsing formation string."""

from fpl.model.managers_models import Formation


def parse_formation(formation_string: str) -> Formation:
    """
    Parse formation string.

    Args:
    ----
        formation_string (str): Formation string.

    Returns:
    -------
        Formation: Formation.

    """
    formation = formation_string.split("-")
    return Formation(
        attackers=int(formation[0]),
        midfielders=int(formation[1]),
        defenders=int(formation[2]),
        goalkeepers=int(formation[3]),
    )

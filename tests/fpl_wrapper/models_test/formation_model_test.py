""" Tests for Formation and PlayerTeam models. """

from fpl_wrapper.model.managers_models import Formation, PlayerTeam
from fpl_wrapper.model.players_models import PlayerData


def test_formation_str():
    """Test formation string representation."""
    formation = Formation(attackers=3, midfielders=4, defenders=3)
    assert str(formation) == "3-4-3-1"


def test_formation_hash():
    """Test formation hash."""
    formation1 = Formation(attackers=3, midfielders=4, defenders=3)
    formation2 = Formation(attackers=3, midfielders=4, defenders=3)
    assert hash(formation1) == hash(formation2)

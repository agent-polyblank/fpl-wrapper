"""Tests for the input_parsing module."""
from fpl.input_parsing.parse_formation import parse_formation


def test_parse_formation():
    """Test the parse_formation function."""
    formation = parse_formation("3-4-3-1")
    assert formation.attackers == 3
    assert formation.midfielders == 4
    assert formation.defenders == 3
    assert formation.goalkeepers == 1

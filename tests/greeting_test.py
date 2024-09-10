"""Example tests."""

import pytest

from src.fpl.example import greeting

@pytest.mark.parametrize(
    argnames=("name", "expected"),
    argvalues=(
        (
            ("Neil", "Hello Neil!"),
            ("Buzz", "Hello Buzz!"),
            ("Michael", "Hello Michael!"),
        )
    ),
    ids=("Test greeting Neil", "Test greeting Buzz", "Test greeting Michael"),
)
def test_greeting(name: str, expected: str) -> None:
    """Test greeting function."""
    assert greeting(name=name) == expected

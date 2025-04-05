"""Test for fixtures module."""

import json
from pytest_mock import mocker
from fpl_wrapper.data_fetch.fixtures import get_fixtures


def test_get_fixtures(fixture_get_event, mocker):
    """test get fixtures."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_get_event
    client.get.return_value = response

    # Call the function with mocks
    result = get_fixtures(client=client, gameweek=0, team_id=0)

    assert len(result.fixtures) == 1

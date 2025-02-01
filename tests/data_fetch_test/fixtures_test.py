"""Test for fixtures module."""

import json
from pytest_mock import mocker
from fpl.data_fetch.fixtures import get_fixtures


def test_get_fixtures(fixture_fixture_get_fixture, mocker):
    """test get fixtures."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_fixture_get_fixture
    client.get.return_value = response

    # Call the function with mocks
    result = get_fixtures(client=client)

    # Add assertions here to validate the result
    assert len(result) == 1

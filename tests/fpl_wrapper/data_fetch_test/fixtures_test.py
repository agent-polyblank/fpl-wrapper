"""Test for fixtures module."""

from fpl_wrapper.data_fetch.fixtures import FixtureProvider


def test_get_fixtures(fixture_get_event, mocker):
    """test get fixtures."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_get_event
    client.get.return_value = response


    fixture_client = FixtureProvider(client)
    # Call the function with mocks
    result = fixture_client.get_fixtures(gameweek=1, team_id=1)

    assert len(result.fixtures) == 1

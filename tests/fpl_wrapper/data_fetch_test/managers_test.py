"""Test the managers data fetch functions."""


from fpl_wrapper.data_fetch.managers import Managers


def test_get_manager_gw_data(mocker, picks_data_no_chip):
    """Test get_manager_gw_data function."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = picks_data_no_chip
    client.get.return_value = response
    managers = Managers(client=client)

    # Call the function with mocks
    result = managers.get_manager_gw_data(team_id=1, gw=1)

    assert result is not None
    assert result.picks[0].element == 201


def test_get_manager_base(mocker, fixture_manager_basic):
    """Test get_manager_base function."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_manager_basic
    client.get.return_value = response
    # Call the function with mocks
    managers = Managers(client=client)

    info = managers.get_manager_basic_info(manager_id=30000)
    assert info.name == "Ricecakes"

def test_get_manager_league_data(mocker, fixture_league_data):
    """Test get_manager_league_data function."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_league_data
    client.get.return_value = response
    # Call the function with mocks
    managers = Managers(client=client)

    league_data = managers.get_league_data(30000, 1)
    assert league_data.new_entries.has_next == False
    assert len(league_data.standings.results) == 50

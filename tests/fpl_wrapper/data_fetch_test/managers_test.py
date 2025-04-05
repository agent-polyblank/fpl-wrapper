from fpl_wrapper.data_fetch.managers import (
    get_league_data,
    get_manager_basic_info,
    get_manager_gw_data,
)
from fpl_wrapper.model.manager_basic import ManagerBase


def test_get_league_data(fixture_league_data, mocker):
    """Test get league data function."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_league_data
    client.get.return_value = response
    # Call the function with mocks
    result = get_league_data(client=client, league_id=1, page=1)

    assert result.league.name == "Arsenal"


def test_get_manager_gw_data(mocker, picks_data_no_chip):
    """Test get_manager_gw_data function."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = picks_data_no_chip
    client.get.return_value = response

    # Call the function with mocks
    result = get_manager_gw_data(client=client, team_id=1, gw=1)

    assert result is not None
    assert result.picks[0].element == 201


def test_get_manager_base(mocker, fixture_manager_basic):
    """Test get_manager_base function."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_manager_basic
    client.get.return_value = response

    info: ManagerBase = get_manager_basic_info(client=client, manager_id=30000)
    assert info.name == "Ricecakes"

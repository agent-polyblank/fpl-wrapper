from fpl_wrapper.data_fetch.players import Players
from fpl_wrapper.model.bootstrap_models import BootstrapData
from fpl_wrapper.model.players_models import PlayerDetail, PlayerData, PlayerSummaryResponse

def test_get_players(mocker, fixture_bootstrap_data):
    """Test get_players returns a dict of player id to PlayerDetail."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_bootstrap_data
    client.get.return_value = response

    mocker.patch(
        "fpl_wrapper.data_fetch.bootstrap_data.get_bootstrap_data",
        return_value=BootstrapData(**fixture_bootstrap_data)
    )

    players = Players(client=client)
    players_dict = players.get_players()

    assert isinstance(players_dict, dict)
    assert all(isinstance(val, PlayerDetail) for val in players_dict.values())

from fpl_wrapper.data_fetch.bootstrap_data import get_bootstrap_data


def test_get_bootstrap_data(fixture_bootstrap_data, mocker):
    """Test get bootstrap data function."""
    client = mocker.Mock()
    response = mocker.Mock()
    response.json.return_value = fixture_bootstrap_data
    client.get.return_value = response
    # Call the function with mocks
    result = get_bootstrap_data(client=client)
    assert result.total_players == 3
    assert result.teams[0].name == "Nott'm Forest"

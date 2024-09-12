import pytest
import httpx
import json
from unittest.mock import MagicMock
from pydantic import ValidationError
from fpl.models import PlayerDetail
from fpl.shared import get_all_player_detail

def test_get_all_player_detail(mocker, bootstrap_data):
    # Mock the httpx.Client.get method to return this mock response
    mock_client = mocker.patch("httpx.Client.get", return_value=MagicMock(text=json.dumps(bootstrap_data)))

    # Create a client instance
    client = httpx.Client()

    # Call the function
    result = get_all_player_detail(client)

    # Verify the result is a list with one PlayerDetail object
    assert len(result) == len(bootstrap_data['elements'])  # Match length of data
    player = result[0]

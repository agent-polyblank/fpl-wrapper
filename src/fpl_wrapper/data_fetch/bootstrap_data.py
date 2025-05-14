"""Fetch bootstrap data from the FPL API."""

import httpx

from fpl_wrapper.model.bootstrap_models import BootstrapData


def get_bootstrap_data(
    client: httpx.Client,
) -> BootstrapData:
    """
    Get all player details from the FPL API.

    Args:
    ----
        client (httpx.Client): HTTP client instance.

    Returns:
    -------
        BootstrapData: Bootstrap data.

    """
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    return BootstrapData(**client.get(url).json())

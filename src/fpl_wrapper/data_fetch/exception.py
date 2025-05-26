"""Custom exceptions for the FPL wrapper module."""


class PhotoNotFoundError(Exception):
    """Exception raised when a photo is not found."""

    def __init__(self, image: str, reason: str) -> None:
        """Initialise PhotoNotFoundError."""
        self.message = f"Photo not found for {image}: {reason}"
        super().__init__(self.message)


class ClubCrestNotFoundError(Exception):
    """Exception raised when a team crest is not found."""

    def __init__(self, team_code: str, team_name: str, reason: str) -> None:
        """Initialise ClubCrestNotFoundError."""
        self.message = (
            f"Club crest not found for {team_code} ({team_name}): {reason}"
        )
        super().__init__(self.message)


class ShirtNotFoundError(Exception):
    """Exception raised when a team shirt is not found."""

    def __init__(self, team_code: str, team_name: str, reason: str) -> None:
        """Initialise ShirtNotFoundError."""
        self.message = (
            f"Shirt not found for {team_code} ({team_name}): {reason}"
        )
        super().__init__(self.message)

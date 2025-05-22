"""Custom exceptions for the FPL wrapper module."""


class PhotoNotFoundError(Exception):
    """Exception raised when a photo is not found."""

    def __init__(self, image: str, reason: str) -> None:
        """Initialise PhotoNotFoundError."""
        self.message = f"Photo not found for {image}: {reason}"
        super().__init__(self.message)

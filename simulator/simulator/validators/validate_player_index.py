import custom_exceptions

class ValidatePlayerIndex:
    """Validates the player index is either 0 or 1"""

    def __init__(self, winner: int) -> None:
        """Gets the winner"""
        self.winner: int = winner

    def validate(self) -> None:
        """Validates the winner"""
        if self.winner not in [0, 1]:
            raise custom_exceptions.InvalidPlayerIndex()

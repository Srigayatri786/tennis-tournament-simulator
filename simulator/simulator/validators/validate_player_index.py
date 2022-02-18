import custom_exceptions

class ValidatePlayerIndex:
    '''
    Validates the player index is either 0 or 1  
    '''
    def __init__(self, winner: int) -> None:
        self.winner: int = winner
        
    def validate(self) -> None:
        if self.winner not in [0, 1]:
            raise custom_exceptions.InvalidPlayerIndex()
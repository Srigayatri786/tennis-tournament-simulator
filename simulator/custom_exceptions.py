from constants import GAME_POINTS
class BaseGameException(Exception):
    """Base Game Exception used"""
    MESSAGE: str = 'Base Exception'

    def __init__(self):
        # Call the base class constructor with the parameters it needs
        super().__init__(self.MESSAGE)


    def __str__(self):
        return self.MESSAGE

class InvalidScoreLengths(BaseGameException):
    """Exception raised when the score lengths are invalid"""
    MESSAGE: str = 'Score lengths are invalid. They must be exactly 2.'

class InvalidPoints(BaseGameException):
    """Exception raised when points are invalid"""
    MESSAGE: str = 'Points must be either 0 or 1'

class InvalidMatchScores(BaseGameException):
    """Exceptionn raised when match scores are invalid"""
    MESSAGE: str = 'Points must be greater than or equal to 0'

class InvalidGameScores(BaseGameException):
    """Exception raised when game scores are invalid"""
    MESSAGE: str = 'Game scores should be one of: ' + ', '.join([str(game_point) for game_point in GAME_POINTS])

class InvalidPlayerIndex(BaseGameException):
    """Exception raised when player index is invalid"""
    MESSAGE: str = 'Player index in a match should be either 0 or 1'

class InvalidNumberServes(BaseGameException):
    """Exception raised when number of serves is invalid"""
    MESSAGE: str = 'Serves should be either 1 or 2'


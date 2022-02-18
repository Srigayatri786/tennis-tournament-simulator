from constants import GAME_POINTS
class BaseGameException(Exception):
    MESSAGE: str = 'Base Exception'

    def __init__(self):
        # Call the base class constructor with the parameters it needs
        super().__init__(self.MESSAGE)


    def __str__(self):
        return self.MESSAGE

class InvalidScoreLengths(BaseGameException):
    MESSAGE: str = 'Score lengths are invalid. They must be exactly 2.'

class InvalidPoints(BaseGameException):
    MESSAGE: str = 'Points must be either 0 or 1'

class InvalidMatchScores(BaseGameException):
    MESSAGE: str = 'Points must be greater than or equal to 0'

class InvalidGameScores(BaseGameException):
    MESSAGE: str = 'Game scores should be one of: ' + ', '.join([str(game_point) for game_point in GAME_POINTS])

class InvalidPlayerIndex(BaseGameException):
    MESSAGE: str = 'Player index in a match should be either 0 or 1'

class InvalidNumberServes(BaseGameException):
    MESSAGE: str = 'Serves should be either 1 or 2'


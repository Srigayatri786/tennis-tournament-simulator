from constants import GAME_POINTS
class BaseException(Exception):
    MESSAGE = 'Base Exception'

    def __init__(self):
        # Call the base class constructor with the parameters it needs
        super().__init__(self.MESSAGE)

    
    def __str__(self):
        return self.MESSAGE

class InvalidScoreLengths(BaseException):
    MESSAGE = 'Score lengths are invalid. They must be exactly 2.'

class InvalidPoints(BaseException):
    MESSAGE = 'Points must be either 0 or 1'

class InvalidMatchScores(BaseException):
    MESSAGE = 'Points must be greater than or equal to 0'

class InvalidGameScores(BaseException):
    MESSAGE = 'Game scores should be one of: ' + ', '.join([str(game_point) for game_point in GAME_POINTS])

class InvalidPlayerIndex(BaseException):
    MESSAGE = 'Player index in a match should be either 0 or 1'


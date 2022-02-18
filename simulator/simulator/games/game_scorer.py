from typing import List
from constants import GAME_POINT, \
    GAME_TYPE, \
    GAME_POINTS, \
    NEXT_GAME_POINTS, \
    POINT_3, \
    ADVANTAGE_POINT, \
    DEUCE
from custom_exceptions import InvalidScoreLengths, InvalidPoints, InvalidGameScores


class GameScorer:

    def get_game_point(self, points: List[int], game_scores: List[GAME_TYPE]):
        '''
        Gets the updated game score given the points and the game scores
        '''

        if len(points) != 2 or len(game_scores) != 2:
            raise InvalidScoreLengths()


        if points[0] == points[1]:
            raise InvalidPoints()
        
        player_1_game_score: GAME_TYPE = self._increase_point(points[0], game_scores[0])
        player_2_game_score: GAME_TYPE = self._increase_point(points[1], game_scores[1])
        
        return self._update_deuce_points([player_1_game_score, player_2_game_score])

    def _increase_point(self, point: int, game_score: GAME_TYPE) -> GAME_TYPE:
        '''
        Increases the game score based on the previous score and the point
        '''

        if point not in [0, 1]:
            raise InvalidPoints()

        if game_score not in GAME_POINTS:
            raise InvalidGameScores()
        
        if not point:
            return game_score
        
        return NEXT_GAME_POINTS[game_score]

    def _update_deuce_points(self, game_scores: List[GAME_TYPE]) -> List[GAME_TYPE]:
        '''
        Updates the game score in case of a Deuce.
        A deuce occurs when the score is tied at 40-40 or when the advatage of a player is lost.
        '''

        if len(game_scores) != 2:
            raise InvalidScoreLengths()
        
        if game_scores[0] == game_scores[1] and (game_scores[0] in [POINT_3, ADVANTAGE_POINT]):
            return [DEUCE, DEUCE]
        return [game_scores[0], game_scores[1]]

    def player_game_point(self, game_scores: List[GAME_TYPE]) -> List[GAME_TYPE]:
        '''
        Returns 0 if player 1 has a game point
        Returns 1 if player 2 has a game point
        Returns -1 otherwise
        '''
        if GAME_POINT not in game_scores:
            return -1
        if game_scores[0] == GAME_POINT:
            return 0
        return 1
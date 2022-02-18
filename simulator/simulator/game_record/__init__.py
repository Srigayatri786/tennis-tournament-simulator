from typing import List
from constants import GAME_RECORD, GAME_TYPE, GAME_POINTS
import custom_exceptions
from validators.validate_scores import ValidateScores

class GameRecord:
    '''
    Maintains a rolling copy of the match between 2 players
    '''

    def __init__(self, round_num: int, player_1: int, player_2: int) -> None:
        '''
        Initializes the match between player 1 and player 2
        '''
        self._scores: List[GAME_TYPE] = GAME_RECORD.copy()
        self._scores['round'] = round_num
        self._scores['player_1_num'] = player_1
        self._scores['player_2_num'] = player_2

    def reset_points(self) -> None:
        '''
        Resets the points to 0
        '''
        self._scores['player_1_point'] = 0
        self._scores['player_2_point'] = 0

    def update_points(self, points: List[int]) -> None:
        '''
        The points must be either 0 or 1.
        Stores whether the player scored a point or not.
        '''
        if len(points) != 2:
            raise custom_exceptions.InvalidScoreLengths

        if points[0] == points[1] or points[0] not in [0, 1] or points[1] not in [0, 1]:
            raise custom_exceptions.InvalidPoints

        self._scores['player_1_point'] = points[0]
        self._scores['player_2_point'] = points[1]

    def get_points(self) -> List[int]:
        '''
        Retrieve the players' points as a list.
        '''
        return [self._scores['player_1_point'], self._scores['player_2_point']]

    def reset_game_scores(self) -> None:
        '''
        Resets the game scores to 0
        '''
        self._scores['player_1_game'] = 0
        self._scores['player_2_game'] = 0

    def update_game_score(self, game_scores: List[GAME_TYPE]) -> None:
        '''
        Updates the game scores
        '''
        if len(game_scores) != 2:
            raise custom_exceptions.InvalidScoreLengths

        if game_scores[0] not in GAME_POINTS or game_scores[1] not in GAME_POINTS:
            raise custom_exceptions.InvalidGameScores

        self._scores['player_1_game'] = game_scores[0]
        self._scores['player_2_game'] = game_scores[1]

    def get_game_scores(self) -> List[GAME_TYPE]:
        '''
        Retrieve the players' game score as a list.
        '''
        return [self._scores['player_1_game'], self._scores['player_2_game']]

    def update_set_score(self, set_scores: List[int]) -> None:
        '''
        Updates the set scores
        '''

        scores_validator = ValidateScores(set_scores)
        scores_validator.validate()

        self._scores['player_1_set'] = set_scores[0]
        self._scores['player_2_set'] = set_scores[1]

    def get_set_scores(self) -> List[int]:
        '''
        Retrieve the players' set score as a list.
        '''
        return [self._scores['player_1_set'], self._scores['player_2_set']]

    def update_match_scores(self, match_scores: List[int]) -> None:
        '''
        Updates the match scores
        '''

        scores_validator = ValidateScores(match_scores)
        scores_validator.validate()

        self._scores['player_1_match'] = match_scores[0]
        self._scores['player_2_match'] = match_scores[1]

    def get_match_scores(self) -> List[int]:
        '''
        Retrieve the players' match scores as a list.
        '''
        return [self._scores['player_1_match'], self._scores['player_2_match']]

    def update_server_information(self, is_player_1_server: bool) -> None:
        '''
        Updates if player 1 is serving
        '''
        self._scores['is_player_1_server'] = int(is_player_1_server)

    def get_server_information(self) -> bool:
        '''
        Retrieves if player 1 is serving
        '''
        return bool(self._scores['is_player_1_server'])

    def update_num_serves(self, num_serves: int) -> None:
        '''
        Updates number of serves it took for serving player. 
        Must be either 1 or 2
        '''
        self._scores['num_serves'] = num_serves

    def get_game_record_information(self) -> List[GAME_TYPE]:
        '''
        Retrieves the records as a list
        '''
        return list(self._scores.values())


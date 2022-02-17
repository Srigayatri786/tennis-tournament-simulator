from simulator.constants import GAME_RECORD

class GameRecord:
    def __init__(self, round, player_1, player_2):
        self._scores = GAME_RECORD.copy()
        self._scores['round'] = round
        self._scores['player_1_num'] = player_1
        self._scores['player_2_num'] = player_2

    def update_points(self, points):
        self._scores['player_1_point'] = points[0]
        self._scores['player_2_point'] = points[1]

    def get_points(self):
        return [self._scores['player_1_point'], self._scores['player_2_point']]

    def update_game_score(self, game_scores):
        self._scores['player_1_game'] = game_scores[0]
        self._scores['player_2_game'] = game_scores[1]

    def get_game_scores(self):
        return [self._scores['player_1_game'], self._scores['player_2_game']]

    def update_set_score(self, set_scores):
        self._scores['player_1_set'] = set_scores[0]
        self._scores['player_2_set'] = set_scores[1]

    def get_set_scores(self):
        return [self._scores['player_1_set'], self._scores['player_2_set']]
    
    def update_match_scores(self, match_scores):
        self._scores['player_1_match'] = match_scores[0]
        self._scores['player_2_match'] = match_scores[1]
    
    def get_match_scores(self):
        return [self._scores['player_1_match'], self._scores['player_2_match']]

    def update_server_information(self, is_player_1_server):
        self._scores['is_player_1_server'] = int(is_player_1_server)
    
    def get_server_information(self):
        return bool(self._scores['is_player_1_server'])
    
    def update_num_serves(self, num_serves):
        self._scores['num_serves'] = num_serves
    
    def get_game_record_information(self):
        return list(self._scores.values())
    
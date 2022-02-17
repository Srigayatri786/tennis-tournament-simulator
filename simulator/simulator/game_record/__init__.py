class GameRecord:
    def __init__(self, round, player_1, player_2):
        self._scores = {
            'player_1_point': 0,
            'player_2_point': 0,
            'player_1_game': 0,
            'player_2_game': 0,
            'player_1_set': 0,
            'player_2_set': 0,
            'player_1_match': 0,
            'player_2_match': 0,
            'round': round,
            'player_1_num': player_1,
            'player_2_num': player_2,
            'is_player_1_server': True,
            'num_serves': 0
        }

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
        self._scores['is_player_1_server'] = is_player_1_server
    
    def get_server_information(self):
        return self._scores['is_player_1_server']
    
    def update_num_serves(self, num_serves):
        self._scores['num_serves'] = num_serves
    
    def get_game_record_information(self):
        return self._scores.values()
    
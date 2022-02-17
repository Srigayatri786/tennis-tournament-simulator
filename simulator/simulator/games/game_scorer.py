from simulator.constants import  NEXT_GAME_POINTS, POINT_3, ADVANTAGE_POINT, DEUCE
from simulator.constants import GAME_POINT
class GameScorer:

    def get_game_point(self, points, game_scores):
        player_1_game_score = self.increase_point(points[0], game_scores[0])
        player_2_game_score = self.increase_point(points[1], game_scores[1])
        return self.update_deuce_points(player_1_game_score, player_2_game_score)

    def increase_point(self, point, game_score):
        if not point:
            return game_score
        
        return NEXT_GAME_POINTS[game_score]

    def update_deuce_points(self, game_score_1, game_score_2):
        if game_score_1 == game_score_2 and (game_score_1 == POINT_3 or game_score_1 == ADVANTAGE_POINT):
            return [DEUCE, DEUCE]
        return [game_score_1, game_score_2]

    def player_game_point(self, game_scores):
        if GAME_POINT not in game_scores:
            return -1
        if game_scores[0] == GAME_POINT:
            return 0
        return 1
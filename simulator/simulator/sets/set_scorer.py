from simulator.constants import GAME_POINT

class SetScorer:
    def get_set_scores(self, set_scores, winner):
        set_scores[winner] += 1
        return set_scores
    
    def is_player_1_serve(self, set_scores):
        return sum(set_scores) % 2 == 0

    def is_tie_breaker(self, set_scores):
        return set_scores[0] == set_scores[1] and set_scores[0] == 6

    def get_set_winner(self, set_scores):
        if self.is_tie_breaker(set_scores) and 7 in set_scores:
            return set_scores.index(7)
        difference = set_scores[0] - set_scores[1]
        if difference >= 2 and set_scores[0] >= 6:
            return 0
        elif difference <= -2 and set_scores[1] >= 6:
            return 1
        
        return -1
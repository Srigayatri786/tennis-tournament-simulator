class MatchScorer:
    def score_match(self, match_scores, set_winner):
        match_scores[set_winner] += 1
        return match_scores
    
    def get_match_winner(self, match_scores):
        if match_scores[0] == 2:
            return 0

        elif match_scores[1] == 2:
            return 1

        return -1

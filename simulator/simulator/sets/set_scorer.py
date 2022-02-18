import custom_exceptions

class SetScorer:

    def get_set_scores(self, set_scores, game_winner):
        '''
        Updates the set score of tthe winner of the game
        '''

        if game_winner not in [0, 1]:
            raise custom_exceptions.InvalidPlayerIndex()
        
        if len(set_scores) != 2:
            raise custom_exceptions.InvalidScoreLengths()

        for score in set_scores:
            if score < 0:
                raise custom_exceptions.InvalidMatchScores()
        
        set_scores[game_winner] += 1
        return set_scores
    
    def is_player_1_serving(self, set_scores, is_player_1_serve):
        '''
        Players change serves whenever odd games (1st, 3rd, 5th etc).
        '''

        if len(set_scores) != 2:
            raise custom_exceptions.InvalidScoreLengths()

        for score in set_scores:
            if score < 0:
                raise custom_exceptions.InvalidMatchScores()

        if sum(set_scores) % 2 == 1:
            return not is_player_1_serve
        return is_player_1_serve

    def is_tie(self, set_scores):
        '''
        A tie is determined if the both players have won 6 games each. A tie breaker is 
        '''
        return set_scores[0] == set_scores[1] and set_scores[0] == 6

    #TODO: fix this
    def get_set_winner(self, set_scores):
        if self.is_tie(set_scores) and 7 in set_scores:
            return set_scores.index(7)
        difference = set_scores[0] - set_scores[1]
        if difference >= 2 and set_scores[0] >= 6:
            return 0
        
        if difference <= -2 and set_scores[1] >= 6:
            return 1
        
        return -1
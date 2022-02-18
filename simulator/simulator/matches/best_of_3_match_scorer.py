from typing import List
from custom_exceptions import InvalidPlayerIndex, InvalidScoreLengths, InvalidMatchScores

class BestOfThreeMatchScorer:
    '''
    The class to score the match: This employs a best of 3 strategy.
    '''
    def score_match(self, match_scores: List[int], set_winner: int) -> List[int]:
        '''
        Updates the match scores of the player who won the set.
        '''
        if set_winner not in [0, 1]:
            raise InvalidPlayerIndex()

        if len(match_scores) != 2:
            raise InvalidScoreLengths()

        for score in match_scores:
            if score < 0:
                raise InvalidMatchScores()

        match_scores[set_winner] += 1
        return match_scores

    def get_match_winner(self, match_scores: List[int]) -> int:
        '''
        Match_Scores -> the scores of both player 1 and player 2
        Returns 0 if player 1 won 2 sets, 
        1 if player 2 won 2 sets, 
        -1 otherwise
        '''
        if len(match_scores) != 2:
            raise InvalidScoreLengths()

        for score in match_scores:
            if score < 0:
                raise InvalidMatchScores()

        winner = -1

        for player, score in enumerate(match_scores):
            if score >= 2:
                return player
        return winner


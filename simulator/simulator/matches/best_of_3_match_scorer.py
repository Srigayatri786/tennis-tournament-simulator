from typing import List
from simulator.validators.validate_scores import ValidateScores
from simulator.validators.validate_player_index import ValidatePlayerIndex

class BestOfThreeMatchScorer:
    """The class to score the match: This employs a best of 3 strategy."""

    def score_match(self, match_scores: List[int], set_winner: int) -> List[int]:
        """Updates the match scores of the player who won the set."""
        player_index_validator = ValidatePlayerIndex(set_winner)
        player_index_validator.validate()

        scores_validator = ValidateScores(match_scores)
        scores_validator.validate()

        match_scores[set_winner] += 1
        return match_scores

    def get_match_winner(self, match_scores: List[int]) -> int:
        """
        Match_Scores -> the scores of both player 1 and player 2
        Returns 0 if player 1 won 2 sets, 
        1 if player 2 won 2 sets, 
        -1 otherwise
        """
        scores_validator = ValidateScores(match_scores)
        scores_validator.validate()

        winner = -1

        for player, score in enumerate(match_scores):
            if score >= 2:
                return player
        return winner


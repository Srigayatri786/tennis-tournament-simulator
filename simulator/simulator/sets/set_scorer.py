from typing import List
from simulator.validators.validate_scores import ValidateScores
from simulator.validators.validate_player_index import ValidatePlayerIndex

class SetScorer:

    def get_set_scores(self, set_scores: List[int], game_winner: int) -> List[int]:
        """Updates the set score of tthe winner of the game"""
        player_index_validator = ValidatePlayerIndex(game_winner)
        player_index_validator.validate()

        scores_validator = ValidateScores(set_scores)
        scores_validator.validate()

        set_scores[game_winner] += 1
        return set_scores

    def is_player_1_serving(self, set_scores: List[int], is_player_1_serve: bool) -> bool:
        """Players change serves whenever odd games (1st, 3rd, 5th etc)."""
        scores_validator = ValidateScores(set_scores)
        scores_validator.validate()

        if sum(set_scores) % 2 == 1:
            return not is_player_1_serve
        return is_player_1_serve

    def _is_tie(self, set_scores: List[int])  -> bool:
        """A tie is determined if the both players have won 6 games each. A tie breaker is """
        return set_scores[0] == set_scores[1] and set_scores[0] == 6

    def get_set_winner(self, set_scores: List[int], prev_set_scores: List[int]) -> int:
        """
        Winner of the set  is he first  to win 6 games with a difference of 2 
        If the game was a tie previously at 6-6, then whoever wins the next round, wins
        """
        scores_validator = ValidateScores(set_scores)
        scores_validator.validate()

        prev_scores_validator = ValidateScores(prev_set_scores)
        prev_scores_validator.validate()

        if self._is_tie(prev_set_scores) and 7 in set_scores:
            return set_scores.index(7)

        difference = set_scores[0] - set_scores[1]
        if difference >= 2 and set_scores[0] >= 6:
            return 0

        if difference <= -2 and set_scores[1] >= 6:
            return 1

        return -1

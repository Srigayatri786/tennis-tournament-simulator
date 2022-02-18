from typing import List
import custom_exceptions

class ValidateScores:
    """
    Validates the scores to make sure  
        there are exactly 2 scores in the array and 
        scores are non-negative
    """

    def __init__(self, scores: List[int]) -> None:
        """Gets the scores"""
        self.scores: List[int] = scores

    def validate(self):
        """Validates the scores according to the above mentioned rules"""
        if len(self.scores) != 2:
            raise custom_exceptions.InvalidScoreLengths()

        for score in self.scores:
            if score < 0:
                raise custom_exceptions.InvalidMatchScores()

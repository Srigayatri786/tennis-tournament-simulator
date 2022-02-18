from typing import List
from unittest import TestCase
import custom_exceptions
from simulator.matches.best_of_3_match_scorer import BestOfThreeMatchScorer

class TestBestOfThreeMatchScorer(TestCase):
    def setUp(self) -> None:
        """Creating a match scorer object"""
        self.match_obj = BestOfThreeMatchScorer()

    def test_set_winner_not_valid(self) -> None:
        """Testing when set winner is not valid"""
        self.assertRaises(
            custom_exceptions.InvalidPlayerIndex, 
            self.match_obj.score_match,
            [1, 1], 2
        ) 

    def test_invalid_match_length_less_than_2(self) -> None:
        """Testing when length of match scores is less than 2."""
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths, 
            self.match_obj.score_match,
            [1], 0 
        )

    def test_invalid_match_length_greater_than_2(self) -> None:
        """Testing when length of match scores is greater than 2"""
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths, 
            self.match_obj.score_match,
            [0, 1, 2], 1
        )

    def test_invalid_match_scores(self) -> None:
        """Testing when match scores are negative"""
        self.assertRaises(
            custom_exceptions.InvalidMatchScores, 
            self.match_obj.score_match,
            [0, -1], 1
        )

    def test_next_points_player_1_wins_1_match(self) -> None:
        """Testing player 1 wins 1  match"""
        match_scores: List[int] = self.match_obj.score_match([0, 0], 0)
        self.assertEqual(match_scores, [1, 0])

    def test_next_points_player_2_wins_1_match(self) -> None:
        """Testing player 2 wins 1 match"""
        match_scores: List[int] = self.match_obj.score_match([0, 0], 1)
        self.assertEqual(match_scores, [0, 1])

    def test_next_points_player_2_wins_2_match(self) -> None:
        """Testing player 2 wins 2 matches"""
        match_scores: List[int] = self.match_obj.score_match([1, 1], 1)
        self.assertEqual(match_scores, [1, 2])

    def test_next_points_player_1_wins_2_match(self) -> None:
        """Testing player 1 wins 2 matches"""
        match_scores: List[int] = self.match_obj.score_match([1, 1], 0)
        self.assertEqual(match_scores, [2, 1])

    def test_winner_invalid_match_length_less_than_2(self) -> None:
        """Testing winner when match scores length is less than 2"""
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.match_obj.get_match_winner, 
            [2]
        )

    def test_winner_invalid_match_length_greater_than_2(self) -> None:
        """Testing winner when match scores length is greater than 2"""
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.match_obj.get_match_winner, 
            [2, 3, 1]
        )

    def test_winner_invalid_match_negative_scores(self) -> None:
        """Testing winner when match scores is negative"""
        self.assertRaises(
            custom_exceptions.InvalidMatchScores,
            self.match_obj.get_match_winner, 
            [2, -3]
        )

    def test_winner_player_1(self) -> None:
        """Get winner whenn player 1 won 2 matches"""
        self.assertEqual(self.match_obj.get_match_winner([2, 1]), 0)

    def test_winner_player_2(self) -> None:
        """Get winner whenn player 2 won 2 matches"""
        self.assertEqual(self.match_obj.get_match_winner([1, 2]), 1)

    def test_winner_player_2_greater_than_2(self) -> None:
        """Get winner whenn player 2 won 3 matches"""
        self.assertEqual(self.match_obj.get_match_winner([1, 3]), 1)

    def test_winner_no_winner_player_1_lead(self) -> None:
        """No winner of the match whenn player 1 is leading"""
        self.assertEqual(self.match_obj.get_match_winner([1, 0]), -1)

    def test_winner_no_winner_player_2_lead(self) -> None:
        """No winner of a match when player 2 is leading"""
        self.assertEqual(self.match_obj.get_match_winner([0, 1]), -1)

    def test_winner_no_winner_blank_match(self) -> None:
        """No winner at beginning of a match"""
        self.assertEqual(self.match_obj.get_match_winner([0, 0]), -1)

    def test_winner_player_both_equal(self) -> None:
        """No winner when both players have a score of 1"""
        self.assertEqual(self.match_obj.get_match_winner([1, 1]), -1)




from typing import List
from unittest import TestCase
import custom_exceptions
from simulator.matches.best_of_3_match_scorer import BestOfThreeMatchScorer

class TestBestOfThreeMatchScorer(TestCase):
    def setUp(self) -> None:
        self.match_obj = BestOfThreeMatchScorer()

    def test_set_winner_not_valid(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidPlayerIndex, 
            self.match_obj.score_match,
            [1, 1], 2
        ) 

    def test_invalid_match_length_less_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths, 
            self.match_obj.score_match,
            [1], 0 
        )

    def test_invalid_match_length_greater_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths, 
            self.match_obj.score_match,
            [0, 1, 2], 1
        )

    def test_invalid_match_scores(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidMatchScores, 
            self.match_obj.score_match,
            [0, -1], 1
        )

    def test_next_points_player_1_wins_1_match(self) -> None:
        match_scores: List[int] = self.match_obj.score_match([0, 0], 0)
        self.assertEqual(match_scores, [1, 0])

    def test_next_points_player_2_wins_1_match(self) -> None:
        match_scores: List[int] = self.match_obj.score_match([0, 0], 1)
        self.assertEqual(match_scores, [0, 1])

    def test_next_points_player_2_wins_2_match(self) -> None:
        match_scores: List[int] = self.match_obj.score_match([1, 1], 1)
        self.assertEqual(match_scores, [1, 2])

    def test_next_points_player_1_wins_2_match(self) -> None:
        match_scores: List[int] = self.match_obj.score_match([1, 1], 0)
        self.assertEqual(match_scores, [2, 1])

    def test_winner_invalid_match_length_less_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.match_obj.get_match_winner, 
            [2]
        )

    def test_winner_invalid_match_length_greater_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.match_obj.get_match_winner, 
            [2, 3, 1]
        )

    def test_winner_invalid_match_negative_scores(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidMatchScores,
            self.match_obj.get_match_winner, 
            [2, -3]
        )

    def test_winner_player_1(self) -> None:
        self.assertEqual(self.match_obj.get_match_winner([2, 1]), 0)

    def test_winner_player_2(self) -> None:
        self.assertEqual(self.match_obj.get_match_winner([1, 2]), 1)

    def test_winner_player_2_greater_than_2(self) -> None:
        self.assertEqual(self.match_obj.get_match_winner([1, 3]), 1)

    def test_winner_no_winner_player_1_lead(self) -> None:
        self.assertEqual(self.match_obj.get_match_winner([1, 0]), -1)

    def test_winner_no_winner_player_2_lead(self) -> None:
        self.assertEqual(self.match_obj.get_match_winner([0, 1]), -1)

    def test_winner_no_winner_blank_match(self) -> None:
        self.assertEqual(self.match_obj.get_match_winner([0, 0]), -1)

    def test_winner_player_both_equal(self) -> None:
        self.assertEqual(self.match_obj.get_match_winner([1, 1]), -1)




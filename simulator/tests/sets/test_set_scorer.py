from unittest import TestCase
from typing import List
import custom_exceptions
from simulator.sets.set_scorer import SetScorer

class TestSetScorer(TestCase):
    def setUp(self) -> None:
        self.set_scorer_obj: SetScorer = SetScorer()

    def test_increase_score_invalid_game_winner(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidPlayerIndex,
            self.set_scorer_obj.get_set_scores,
            [0, 0], 2
        )

    def test_increase_score_invalid_set_scores_length_less_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_scores,
            [0], 0
        )

    def test_increase_score_invalid_set_scores_length_greater_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_scores,
            [0, 0, 0], 1
        )

    def test_increase_score_for_player_1(self) -> None:
        self.assertEqual(
            self.set_scorer_obj.get_set_scores([2, 5], 0),
            [3, 5]
        )

    def test_increase_score_for_player_2(self) -> None:
        self.assertEqual(
            self.set_scorer_obj.get_set_scores([2, 5], 1),
            [2, 6]
        )

    def test_get_server_invalid_set_scores_length_less_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.is_player_1_serving,
            [0], False
        )

    def test_get_server_invalid_set_scores_length_greater_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.is_player_1_serving,
            [0, 0, 0], True
        )

    def test_get_server_when_player_1_serves(self) -> None:
        self.assertEqual(
            self.set_scorer_obj.is_player_1_serving([2, 1], True),
            False
        )

    def test_get_server_when_player_1_serves(self) -> None:
        self.assertEqual(
            self.set_scorer_obj.is_player_1_serving([0, 2], False),
            False
        )

    def test_get_server_when_player_1_serves(self) -> None:
        self.assertEqual(
            self.set_scorer_obj.is_player_1_serving([1, 1], True),
            True
        )

    def test_get_server_when_player_1_serves(self) -> None:
        self.assertEqual(
            self.set_scorer_obj.is_player_1_serving([1, 2], False),
            True
        )

    def test_get_winner_invalid_set_scores_length_less_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_winner,
            [0], [0, 0]
        )

    def test_get_winner_invalid_set_scores_length_greater_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_winner,
            [0, 0, 0], [1, 0]
        )

    def test_get_winner_invalid_set_prev_scores_length_less_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_winner,
            [1,  0],  [0]
        )

    def test_get_winner_invalid_set_prev_scores_length_greater_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_winner,
            [0, 0], [1, 0, 1]
        )

    def test_get_winner_no_winner(self) -> None:
        self.assertEqual(self.set_scorer_obj.get_set_winner([1, 0], [0, 0]), -1)

    def test_get_winner_player_1_winner(self) -> None:
        self.assertEqual(self.set_scorer_obj.get_set_winner([6, 4], [1, 0]), 0)

    def test_get_winner_player_2_winner(self) -> None:
        self.assertEqual(self.set_scorer_obj.get_set_winner([4, 6], [0, 1]), 1)

    def test_get_winner_player_1_no_winner(self) -> None:
        self.assertEqual(self.set_scorer_obj.get_set_winner([6, 5], [1, 0]), -1)

    def test_get_winner_player_1_winner_greater_than_6(self) -> None:
        self.assertEqual(self.set_scorer_obj.get_set_winner([7, 5], [1, 0]), 0)

    def test_get_winner_player_2_no_winner(self) -> None:
        self.assertEqual(self.set_scorer_obj.get_set_winner([5, 6], [0, 1]), -1)

    def test_get_winner_player_2_winner_greater_than_6(self) -> None:
        self.assertEqual(self.set_scorer_obj.get_set_winner([5, 7], [0, 1]), 1)

    def test_get_winner_no_winner_tie(self) -> None:
        self.assertEqual(self.set_scorer_obj.get_set_winner([6, 6], [0, 1]), -1)

    def test_get_winner_tie_breaker_player_1(self) -> None:
        self.assertEqual(self.set_scorer_obj.get_set_winner([7, 6], [6, 6]), 0)

    def test_get_winner_tie_breaker_player_1(self) -> None:
        self.assertEqual(self.set_scorer_obj.get_set_winner([6, 7], [6, 6]), 1)

from unittest import TestCase
from typing import List
import custom_exceptions
from simulator.sets.set_scorer import SetScorer

class TestSetScorer(TestCase):
    def setUp(self) -> None:
        '''
        Creating the set scorer object
        '''
        self.set_scorer_obj: SetScorer = SetScorer()

    def test_increase_score_invalid_game_winner(self) -> None:
        '''
        Testing when there is an invalid game winner
        '''
        self.assertRaises(
            custom_exceptions.InvalidPlayerIndex,
            self.set_scorer_obj.get_set_scores,
            [0, 0], 2
        )

    def test_increase_score_invalid_set_scores_length_less_than_2(self) -> None:
        '''
        Testing when the game scores < 2
        '''
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_scores,
            [0], 0
        )

    def test_increase_score_invalid_set_scores_length_greater_than_2(self) -> None:
        '''
        Testing when game scores > 2
        '''
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_scores,
            [0, 0, 0], 1
        )

    def test_increase_score_for_player_1(self) -> None:
        '''
        Test Player 1 won a set
        '''
        self.assertEqual(
            self.set_scorer_obj.get_set_scores([2, 5], 0),
            [3, 5]
        )

    def test_increase_score_for_player_2(self) -> None:
        '''
        Test Player 2 won a set
        '''
        self.assertEqual(
            self.set_scorer_obj.get_set_scores([2, 5], 1),
            [2, 6]
        )

    def test_get_server_invalid_set_scores_length_less_than_2(self) -> None:
        '''
        Test scores length is less than 2 while getting server information
        '''
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.is_player_1_serving,
            [0], False
        )

    def test_get_server_invalid_set_scores_length_greater_than_2(self) -> None:
        '''
        Test scores length is greater than 2 while getting server information
        '''
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.is_player_1_serving,
            [0, 0, 0], True
        )

    def test_get_server_when_player_1_serves_odd(self) -> None:
        '''
        Test server information when player 1 serves and odd games have been played
        '''
        self.assertEqual(
            self.set_scorer_obj.is_player_1_serving([2, 1], True),
            False
        )

    def test_get_server_when_player_2_serves_even(self) -> None:
        '''
        Test server information when player 2 serves and even games have been played
        '''
        self.assertEqual(
            self.set_scorer_obj.is_player_1_serving([0, 2], False),
            False
        )

    def test_get_server_when_player_1_serves_even(self) -> None:
        '''
        Test server informationn when player 1 serves and even games have been played
        '''
        self.assertEqual(
            self.set_scorer_obj.is_player_1_serving([1, 1], True),
            True
        )

    def test_get_server_when_player_2_serves_odd(self) -> None:
        '''
        Test server informationn when player 2 serves and odd games have been played
        '''
        self.assertEqual(
            self.set_scorer_obj.is_player_1_serving([1, 2], False),
            True
        )

    def test_get_winner_invalid_set_scores_length_less_than_2(self) -> None:
        '''
        Test winner with length of set scores < 2
        '''
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_winner,
            [0], [0, 0]
        )

    def test_get_winner_invalid_set_scores_length_greater_than_2(self) -> None:
        '''
        Test winner with length of set scores > 2
        '''
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_winner,
            [0, 0, 0], [1, 0]
        )

    def test_get_winner_invalid_set_prev_scores_length_less_than_2(self) -> None:
        '''
        Test winner with length of previous set scores < 2
        '''
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_winner,
            [1,  0],  [0]
        )

    def test_get_winner_invalid_set_prev_scores_length_greater_than_2(self) -> None:
        '''
        Test winner with length of previous set scores > 2
        '''
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.set_scorer_obj.get_set_winner,
            [0, 0], [1, 0, 1]
        )

    def test_get_winner_no_winner(self) -> None:
        '''
        Test no winner
        '''
        self.assertEqual(self.set_scorer_obj.get_set_winner([1, 0], [0, 0]), -1)

    def test_get_winner_player_1_winner(self) -> None:
        '''
        Test player 1 is the winner of the game
        '''
        self.assertEqual(self.set_scorer_obj.get_set_winner([6, 4], [1, 0]), 0)

    def test_get_winner_player_2_winner(self) -> None:
        '''
        Test player 2 is the winner of the game
        '''
        self.assertEqual(self.set_scorer_obj.get_set_winner([4, 6], [0, 1]), 1)

    def test_get_winner_player_1_no_winner(self) -> None:
        '''
        Test no winner when player 1 won 6 games
        '''
        self.assertEqual(self.set_scorer_obj.get_set_winner([6, 5], [1, 0]), -1)

    def test_get_winner_player_1_winner_greater_than_6(self) -> None:
        '''
        Test player 1 winner when player 1 won 7 games
        '''
        self.assertEqual(self.set_scorer_obj.get_set_winner([7, 5], [1, 0]), 0)

    def test_get_winner_player_2_no_winner(self) -> None:
        '''
        Test no winner when player 2 won 6 games
        '''
        self.assertEqual(self.set_scorer_obj.get_set_winner([5, 6], [0, 1]), -1)

    def test_get_winner_player_2_winner_greater_than_6(self) -> None:
        '''
        Test player 2 winner when player 1 won 7 games
        '''
        self.assertEqual(self.set_scorer_obj.get_set_winner([5, 7], [0, 1]), 1)

    def test_get_winner_no_winner_tie(self) -> None:
        '''
        Test no winner when both player has won 6 games
        '''
        self.assertEqual(self.set_scorer_obj.get_set_winner([6, 6], [0, 1]), -1)

    def test_get_winner_tie_breaker_player_1(self) -> None:
        '''
        Test player 1 when there was a tie breaker
        '''
        self.assertEqual(self.set_scorer_obj.get_set_winner([7, 6], [6, 6]), 0)

    def test_get_winner_tie_breaker_player_2(self) -> None:
        '''
        Test player 2 when there was a tie breaker
        '''
        self.assertEqual(self.set_scorer_obj.get_set_winner([6, 7], [6, 6]), 1)

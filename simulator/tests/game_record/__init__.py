from unittest import TestCase
from typing import List
from simulator.game_record import GameRecord
from constants import GAME_RECORD, GAME_TYPE
import custom_exceptions

class TestGameRecord(TestCase):
    def setUp(self) -> None:
        """
        Create a game record
        """
        self.game_record = GameRecord(round_num=1, player_1=2, player_2=3)
        self.game_record_columns = list(GAME_RECORD.keys())

    def get_game_record(self) -> List[GAME_TYPE]:
        """
        Get the game record
        """
        return self.game_record.get_game_record_information()

    def test_round(self) -> None:
        """
        Test the round number
        """
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(game_record[self.game_record_columns.index('round')], 1)

    def test_player_1(self) -> None:
        """
        Test player 1 number
        """
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(game_record[self.game_record_columns.index('player_1_num')], 2)

    def test_player_2(self) -> None:
        """
        Test player 2 number
        """
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(game_record[self.game_record_columns.index('player_2_num')], 3)

    def test_reset_points(self) -> None:
        """
        Test that reset points works
        """
        self.game_record.update_points([0, 1])
        self.game_record.reset_points()
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(game_record[self.game_record_columns.index('player_2_point')], 0)
        self.assertEqual(game_record[self.game_record_columns.index('player_1_point')], 0)

    def test_points_in_record(self) -> None:
        """
        Update the points in the record
        """
        self.game_record.update_points([0, 1])
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(game_record[self.game_record_columns.index('player_1_point')], 0)
        self.assertEqual(game_record[self.game_record_columns.index('player_2_point')], 1)

    def test_points_get_record(self) -> None:
        """
        Update the points and test the get points function
        """
        self.game_record.update_points([0, 1])
        self.assertEqual(self.game_record.get_points(), [0, 1])

    def test_points_with_one_point(self) -> None:
        """
        Test with points length < 2
        """
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.game_record.update_points,
            [1]
        )

    def test_points_with_more_than_two_point(self) -> None:
        """
        Test with points length > 2
        """
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.game_record.update_points,
            [1, 0, 1]
        )

    def test_same_points(self) -> None:
        """
        Test with same points.
        """
        self.assertRaises(
            custom_exceptions.InvalidPoints,
            self.game_record.update_points,
            [1, 1]
        )

    def test_not_valid_points(self) -> None:
        """
        Test with points that are not valid
        """
        self.assertRaises(
            custom_exceptions.InvalidPoints,
            self.game_record.update_points,
            [1, 2]
        )

    def test_reset_game(self) -> None:
        """
        Test the reset game function
        """
        self.game_record.update_game_score([0, 15])
        self.game_record.reset_game_scores()
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(game_record[self.game_record_columns.index('player_1_game')], 0)
        self.assertEqual(game_record[self.game_record_columns.index('player_2_game')], 0)

    def test_get_game_scores(self) -> None:
        """
        Test the get game scores
        """
        self.game_record.update_game_score([0, 15])
        self.assertEqual(self.game_record.get_game_scores(), [0, 15])

    def test_game(self) -> None:
        """
        Test game scores with valid point for player 2
        """
        self.game_record.update_game_score([0, 15])
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(game_record[self.game_record_columns.index('player_1_game')], 0)
        self.assertEqual(game_record[self.game_record_columns.index('player_2_game')], 15)

    def test_game_with_one_point(self) -> None:
        """
        Test game scores with scores length < 2 
        """
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.game_record.update_game_score,
            [40]
        )

    def test_game_with_more_than_two_point(self) -> None:
        """
        Test game scores with scores length > 2 
        """
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.game_record.update_game_score,
            [40, 0, 15]
        )

    def test_not_valid_game(self) -> None:
        """
        Test not valid game score
        """
        self.assertRaises(
            custom_exceptions.InvalidGameScores,
            self.game_record.update_game_score,
            [1, 1]
        )

    def test_get_set_scores(self) -> None:
        """
        Test the get set scores
        """
        self.game_record.update_set_score([2, 5])
        self.assertEqual(self.game_record.get_set_scores(), [2, 5])

    def test_set(self) -> None:
        """
        Test set scores with valid scores
        """
        self.game_record.update_set_score([2, 3])
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(game_record[self.game_record_columns.index('player_1_set')], 2)
        self.assertEqual(game_record[self.game_record_columns.index('player_2_set')], 3)

    def test_set_with_one_point(self) -> None:
        """
        Test set scores with scores length < 2 
        """
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.game_record.update_set_score,
            [2]
        )

    def test_set_with_more_than_two_point(self) -> None:
        """
        Test set scores with scores length > 2 
        """
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.game_record.update_set_score,
            [2, 0, 3]
        )

    def test_not_valid_set(self) -> None:
        """
        Test not valid set score
        """
        self.assertRaises(
            custom_exceptions.InvalidMatchScores,
            self.game_record.update_set_score,
            [-1, 1]
        )


    def test_get_match_scores(self) -> None:
        """
        Test the get match scores
        """
        self.game_record.update_match_scores([2, 1])
        self.assertEqual(self.game_record.get_match_scores(), [2, 1])

    def test_match(self) -> None:
        """
        Test match scores with valid scores
        """
        self.game_record.update_match_scores([1, 2])
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(game_record[self.game_record_columns.index('player_1_match')], 1)
        self.assertEqual(game_record[self.game_record_columns.index('player_2_match')], 2)

    def test_match_with_one_point(self) -> None:
        """
        Test match scores with scores length < 2 
        """
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.game_record.update_match_scores,
            [2]
        )

    def test_match_with_more_than_two_point(self) -> None:
        """
        Test match scores with scores length > 2 
        """
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths,
            self.game_record.update_match_scores,
            [2, 0, 1]
        )

    def test_not_valid_match(self) -> None:
        """
        Test not valid match score
        """
        self.assertRaises(
            custom_exceptions.InvalidMatchScores,
            self.game_record.update_match_scores,
            [-1, 0]
        )

    def test_update_server_information_player_1(self) -> None:
        """
        Test when player 1 is server
        """
        self.game_record.update_server_information(True)
        self.assertEqual(
            self.game_record.get_server_information(), True
        )

    def test_update_server_information_from_record_player_1(self) -> None:
        """
        Test when player 1 is server from record
        """
        self.game_record.update_server_information(True)
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(
            game_record[self.game_record_columns.index('is_player_1_server')], 1
        )

    def test_update_server_information_player_2(self) -> None:
        """
        Test when player 1 is server
        """
        self.game_record.update_server_information(False)
        self.assertEqual(
            self.game_record.get_server_information(), False
        )

    def test_update_server_information_from_record_player_2(self) -> None:
        """
        Test when player 1 is server from record
        """
        self.game_record.update_server_information(False)
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(
            game_record[self.game_record_columns.index('is_player_1_server')], 0
        )

    def test_invalid_num_serves(self) -> None:
        """
        Test the number of serves with an invalid number
        """
        self.assertRaises(
            custom_exceptions.InvalidNumberServes,
            self.game_record.update_num_serves,
            4
        )

    def test_num_serves_2_from_record(self) -> None:
        """
        Test the number of serves with an invalid number
        """
        self.game_record.update_num_serves(2)
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(
            game_record[self.game_record_columns.index('num_serves')], 2
        )

    def test_num_serves_1_from_record(self) -> None:
        """
        Test the number of serves with an invalid number
        """
        self.game_record.update_num_serves(1)
        game_record: List[GAME_TYPE] = self.get_game_record()
        self.assertEqual(
            game_record[self.game_record_columns.index('num_serves')], 1
        )

    def test_num_serves_2_from_func(self) -> None:
        """
        Test the number of serves with an invalid number
        """
        self.game_record.update_num_serves(2)
        self.assertEqual(
            self.game_record.get_num_serves(), 2
        )

    def test_num_serves_1_from_func(self) -> None:
        """
        Test the number of serves with an invalid number
        """
        self.game_record.update_num_serves(1)
        self.assertEqual(
            self.game_record.get_num_serves(), 1
        )






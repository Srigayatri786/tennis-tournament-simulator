from unittest import TestCase
from typing import List
from simulator.game_record import GameRecord
from constants import GAME_RECORD, GAME_TYPE, POINT_0, POINT_1, POINT_2

# TODO: Finish all test cases
class TestGameRecord(TestCase):
    def setUp(self) -> None:
        self.game_record = GameRecord(round=1, player_1=2, player_2=3)
        self.game_record_columns = list(GAME_RECORD.keys())

    # def get_game_record(self) -> List[GAME_TYPE]:
    #     return self.game_record.get_game_record_information()

    # def test_round(self) -> None:
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('round')], 1)

    # def test_player_1(self) -> None:
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_1_num')], 2)
    
    # def test_player_2(self) -> None:
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_num')], 3)

    # def test_reset_points(self) -> None:
    #     self.game_record.update_points([0, 1])
    #     self.game_record.reset_points()
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_point'), 0])
    #     self.assertEqual(game_record[self.game_record_columns.index('player_1_point'), 0])

    # def test_points(self) -> None:
    #     self.game_record.reset_points()
    #     self.game_record.update_points([0, 1])
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_point'), 1])
    
    # def test_points_with_one_point(self) -> None:
    #     self.game_record.reset_points()
    #     self.game_record.update_points([1])
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_point'), 0])
    #     self.assertEqual(game_record[self.game_record_columns.index('player_1_point'), 0])

    # def test_points_with_more_than_two_point(self) -> None:
    #     self.game_record.reset_points()
    #     self.game_record.update_points([1, 0, 0])
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_point'), 0])
    #     self.assertEqual(game_record[self.game_record_columns.index('player_1_point'), 1])
    
    # def test_same_points(self) -> None:
    #     self.game_record.reset_points()
    #     self.game_record.update_points([1, 1])
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_point'), 0])
    #     self.assertEqual(game_record[self.game_record_columns.index('player_1_point'), 0])

    # def test_not_valid_points(self) -> None:
    #     self.game_record.reset_points()
    #     self.game_record.update_points([1, 2])
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_point'), 0])
    #     self.assertEqual(game_record[self.game_record_columns.index('player_1_point'), 1])

    # def test_reset_game(self) -> None:
    #     self.game_record.update_game_score([0, 15])
    #     self.game_record.reset_game_scores()
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_1_game'), 0])
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_game'), 0])

    # def test_game(self) -> None:
    #     self.game_record.reset_game_scores()
    #     self.game_record.update_game_score([0, 15])
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_game'), 15])
    
    # def test_game_with_one_point(self) -> None:
    #     self.game_record.reset_game_scores()
    #     self.game_record.update_game_score([40])
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_1_game'), 0])
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_game'), 0])

    # def test_game_with_more_than_two_point(self) -> None:
    #     self.game_record.reset_game_scores()
    #     self.game_record.update_game_score([, 0, 0])
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_1_game'), 0])
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_game'), 1])
    
    # def test_not_valid_game(self) -> None:
    #     self.game_record.reset_game_scores()
    #     self.game_record.update_game_score([1, 1])
    #     game_record: List[GAME_TYPE] = self.get_game_record()
    #     self.assertEqual(game_record[self.game_record_columns.index('player_1_game'), 0])
    #     self.assertEqual(game_record[self.game_record_columns.index('player_2_game'), 0])
    

    

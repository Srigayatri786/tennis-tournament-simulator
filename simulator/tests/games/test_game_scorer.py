from typing import List
from unittest import TestCase
from constants import GAME_TYPE, GAME_POINT, DEUCE, ADVANTAGE_POINT
from simulator.games.game_scorer import GameScorer
import custom_exceptions

class TestGameScorer(TestCase):
    def setUp(self) -> None:
        self.game_scorer_obj: GameScorer = GameScorer()
    
    def test_invalid_point_length_less_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths, 
            self.game_scorer_obj.get_game_point,
            [0], [0, 15]
        )
    
    def test_invalid_point_length_greater_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths, 
            self.game_scorer_obj.get_game_point,
            [0, 1, 1], [0, 15]
        )

    def test_invalid_game_length_less_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths, 
            self.game_scorer_obj.get_game_point,
            [0, 1], [0]
        )
    
    def test_invalid_game_length_greater_than_2(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidScoreLengths, 
            self.game_scorer_obj.get_game_point,
            [0, 1], [0, 15, 30]
        )

    def test_point_not_valid_range(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidPoints, 
            self.game_scorer_obj.get_game_point,
            [0, 2], [0, 15]
        )

    def test_point_not_valid_both_equal(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidPoints, 
            self.game_scorer_obj.get_game_point,
            [0, 0], [0, 15]
        )
    
    def test_game_score_not_valid(self) -> None:
        self.assertRaises(
            custom_exceptions.InvalidGameScores, 
            self.game_scorer_obj.get_game_point,
            [0, 1], [0, 1]
        )

    def test_next_points_player_2_scores_1_point(self) -> None:
        game_scores: List[GAME_TYPE] = self.game_scorer_obj.get_game_point([0, 1], [0, 0])
        self.assertEqual(game_scores, [0, 15])

    def test_next_points_player_2_scores_2_point(self) -> None:
        game_scores: List[GAME_TYPE] = self.game_scorer_obj.get_game_point([0, 1], [0, 15])
        self.assertEqual(game_scores, [0, 30])

    def test_next_points_player_2_scores_3_point(self) -> None:
        game_scores: List[GAME_TYPE] = self.game_scorer_obj.get_game_point([0, 1], [0, 30])
        self.assertEqual(game_scores, [0, 40])

    def test_next_points_player_2_scores_game_point(self) -> None:
        game_scores: List[GAME_TYPE] = self.game_scorer_obj.get_game_point([0, 1], [0, 40])
        self.assertEqual(game_scores, [0, GAME_POINT])
    
    def test_next_points_deuce_player_2_starts_deuce(self) -> None:
        game_scores: List[GAME_TYPE] = self.game_scorer_obj.get_game_point([0, 1], [40, 30])
        self.assertEqual(game_scores, [DEUCE, DEUCE])

    def test_next_points_deuce_player_1_starts_deuce(self) -> None:
        game_scores: List[GAME_TYPE] = self.game_scorer_obj.get_game_point([1, 0], [30, 40])
        self.assertEqual(game_scores, [DEUCE, DEUCE])

    def test_next_points_deuce_player_1_deuces_with_advantage(self) -> None:
        game_scores: List[GAME_TYPE] = self.game_scorer_obj.get_game_point(
            [0, 1], [ADVANTAGE_POINT, DEUCE]
        )
        self.assertEqual(game_scores, [DEUCE, DEUCE])


    def test_next_points_deuce_player_1_wins_with_advantage(self) -> None:
        game_scores: List[GAME_TYPE] = self.game_scorer_obj.get_game_point(
            [1, 0], [ADVANTAGE_POINT, DEUCE]
        )
        self.assertEqual(game_scores, [GAME_POINT, DEUCE])


    def test_next_points_deuce_player_2_deuces_with_advantage(self) -> None:
        game_scores: List[GAME_TYPE] = self.game_scorer_obj.get_game_point(
            [1, 0], [DEUCE, ADVANTAGE_POINT]
        )
        self.assertEqual(game_scores, [DEUCE, DEUCE])


    def test_next_points_deuce_player_2_wins_with_advantage(self) -> None:
        game_scores: List[GAME_TYPE] = self.game_scorer_obj.get_game_point(
            [0, 1], [DEUCE, ADVANTAGE_POINT]
        )
        self.assertEqual(game_scores, [DEUCE, GAME_POINT])

    
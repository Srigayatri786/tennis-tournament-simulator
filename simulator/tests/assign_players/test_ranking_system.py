from unittest import TestCase
from simulator.assign_players.ranking_system import RankingSystem

class TestRankingSystem(TestCase):
    def setUp(self) -> None:
        """Creates the object necessary to test the rankinng system"""
        self.ranking_system_obj = RankingSystem()

    def test_assign_players_even(self) -> None:
        """Testing even number of players"""
        player_pairs = self.ranking_system_obj.assign_players_to_rounds(range(1, 5))
        expected_player_pairs = [(1, 4), (2, 3)]

        self.assertCountEqual(player_pairs, expected_player_pairs)

    def test_assign_players_odd(self) -> None:
        """Testing odd number of players"""
        player_pairs = self.ranking_system_obj.assign_players_to_rounds(range(1, 6))
        expected_player_pairs = [(1, 5), (2, 4), (None, 3)]

        self.assertCountEqual(player_pairs, expected_player_pairs)

    def test_one_player(self) -> None:
        """Testing with 1 player"""
        player_pairs = self.ranking_system_obj.assign_players_to_rounds([1])
        expected_player_pairs = [(None, 1)]

        self.assertCountEqual(player_pairs, expected_player_pairs)

    def test_zero_players(self) -> None:
        """Testing an empty list of players"""
        player_pairs = self.ranking_system_obj.assign_players_to_rounds([])
        expected_player_pairs = []

        self.assertCountEqual(player_pairs, expected_player_pairs)

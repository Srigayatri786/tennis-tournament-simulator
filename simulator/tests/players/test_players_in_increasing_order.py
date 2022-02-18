from typing import List
from unittest import TestCase
from simulator.players.player_in_increasing_order import PlayersIncreasingOrder

class TestPlayersIncreasingOrder(TestCase):
    def setUp(self) -> None:
        """Creating objects used for testing"""
        self.num_players: int = 35

        self.players_obj: PlayersIncreasingOrder = PlayersIncreasingOrder(self.num_players)
        self.players: List[int] = self.players_obj.simulate_list_of_players()

    def test_simulate_player(self):
        """Test player generation"""
        self.assertCountEqual(self.players, [i + 1 for i in range(self.num_players)])

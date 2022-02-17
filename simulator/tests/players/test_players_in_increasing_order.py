import unittest
from simulator.players.player_in_increasing_order import PlayersIncreasingOrder

class TestPlayersIncreasingOrder(unittest.TestCase):
    def setUp(self) -> None:
        self.num_players = 35

        self.players_obj = PlayersIncreasingOrder(self.num_players)
        self.players = self.players_obj.simulate_list_of_players()

    def test_type_of_players(self):
        self.assertIsInstance(self.players, list)

    def test_type_player_id(self):
        for player_num in self.players:
            self.assertIsInstance(player_num, int)
    
    def test_simulate_player(self):
        self.assertCountEqual(self.players, [i + 1 for i in range(self.num_players)])
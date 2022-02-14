import unittest
from simulator.simulator.players.player_in_increasing_order import PlayersIncreasingOrder

class TestPlayers(unittest.TestCase):
    def setUp(self) -> None:
        self.num_players = 35

    def test_simulate_player(self):
        players_obj = PlayersIncreasingOrder(self.num_players)
        players = players_obj.simulate_list_of_players()

        # Assert
        actual_list_of_players = [i + 1 for i in range(self.num_players)]
        self.assertCountEqual(players, actual_list_of_players)
from simulator.players.player_in_increasing_order import PlayersIncreasingOrder

class Simulator:
    def __init__(self, num_players):
        self.num_players = num_players

    def simulate_tennis_tournament(self):
        players_obj = PlayersIncreasingOrder(self.num_players)
        players = players_obj.simulate_list_of_players()

        print(players)
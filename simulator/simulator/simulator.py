from simulator.players.player_in_increasing_order import PlayersIncreasingOrder
from simulator.assign_players.ranking_system import RankingSystem
from simulator.simulate_match import MatchSimulator
from constants import GAME_RECORD

class Simulator:
    def __init__(self, num_players: int) -> None:
        self.num_players = num_players
        self.winner = -1
        self.all_logs = [[GAME_RECORD.keys()]]

    def simulate_tennis_tournament(self):
        players_obj = PlayersIncreasingOrder(self.num_players)
        players: int = players_obj.simulate_list_of_players()
        
        ranking_system_obj = RankingSystem()
        round = 1

        while len(players) > 1:
            player_pairs = ranking_system_obj.assign_players_to_rounds(players)
            winners = []
            for player_1, player_2 in player_pairs:
                if player_1 and player_2:

                    match_simulator = MatchSimulator(round, player_1, player_2)
                    winner = match_simulator.simulate_match()
                    winners.append(winner)

                    match_logs = match_simulator.get_match_logs()
                    self.all_logs.append(match_logs)

                elif player_1:
                    winners.append(player_1)
                else:
                    winners.append(player_2)

            players = winners
            round += 1
        self.winner = players[0]
    
    def get_winner(self):
        return self.winner
    
    def get_logs(self):
        return [log for match_logs in self.all_logs for log in match_logs]


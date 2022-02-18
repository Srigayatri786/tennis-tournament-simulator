from typing import List
from simulator.constants import GAME_TYPE
from simulator.players.player_in_increasing_order import PlayersIncreasingOrder
from simulator.assign_players.ranking_system import RankingSystem
from simulator.simulate_match import MatchSimulator
from constants import GAME_RECORD

class Simulator:
    """Simulates a tournament for the specified number of players"""

    def __init__(self, num_players: int) -> None:
        self.num_players: int = num_players
        self.winner: int = -1
        self.all_logs: List[List[GAME_TYPE]] = [[GAME_RECORD.keys()]]
        self.ranking_system_obj: RankingSystem = RankingSystem()
        self.players_obj: PlayersIncreasingOrder = PlayersIncreasingOrder(self.num_players)
        self.players: List[int] = self.players_obj.simulate_list_of_players()

    def simulate_tennis_tournament(self):
        """Simulates the Tennis tournament"""
        round_num = 1

        while len(self.players) > 1:
            # pairs players together
            player_pairs = self.ranking_system_obj.assign_players_to_rounds(self.players)
            
            winners = []
            for player_1, player_2 in player_pairs:
                # simulate a match between player_1 and player_2
                if player_1 and player_2:
                    match_simulator = MatchSimulator(round_num, player_1, player_2)
                    winner = match_simulator.simulate_match()
                    winners.append(winner)

                    match_logs = match_simulator.get_match_logs()
                    self.all_logs.append(match_logs)

                elif player_1:
                    winners.append(player_1)
                else:
                    winners.append(player_2)

            # winners of current round will be the players of the next round
            self.players = winners
            round_num += 1
        
        # the winner of tournament is the first element of the players list
        return self.players[0]

    def get_logs(self):
        """Retrives the logs"""
        return [log for match_logs in self.all_logs for log in match_logs]


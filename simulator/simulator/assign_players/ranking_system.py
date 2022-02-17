from simulator.assign_players import AssignPlayers

class RankingSystem(AssignPlayers):
    """
    This implementation assigns the strongest player to the weakest player
    Assumption: The players are sorted from strongest to weakest
    """
    def assign_players_to_rounds(self, players):
        player_pairs = []

        mid_point = len(players) // 2
        strong_players = players[:mid_point]
        weak_players = players[mid_point:][::-1]

        for i in range(len(weak_players)):
            player_1 = None
            if i < len(strong_players):
                player_1 = strong_players[i]
            
            player_pairs.append((player_1, weak_players[i]))
        
        return player_pairs

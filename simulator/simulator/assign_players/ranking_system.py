import itertools
from simulator.assign_players import AssignPlayers
from itertools import zip_longest
from typing import List, Tuple

class RankingSystem(AssignPlayers):
    """
    This implementation assigns the strongest player to the weakest player
    Assumption: The players are sorted from strongest to weakest
    """
    def assign_players_to_rounds(self, players: List[int]) -> List[Tuple[int]]:
        """
        The players are divided into 2 arrays
        Strong players are the first half, while the weak players are the second half.
        The weak players array is reversed and then combined 

        For instance if the players are [1,2,3,4,5]:
        then strong array: [1,2]
        weak array: [3,4,5] 
        weak array reversed = [5,4,3]

        combining strong array with the weak array: (1,5), (2,4), (None, 3)
        """

        mid_point: int = len(players) // 2
        strong_players: List[int] = players[:mid_point]
        weak_players: List[int] = players[mid_point:][::-1]

        return list(zip_longest(strong_players, weak_players))

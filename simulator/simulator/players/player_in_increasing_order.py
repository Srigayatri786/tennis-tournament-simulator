from typing  import List
from simulator.players import Players

class PlayersIncreasingOrder(Players):
    def simulate_list_of_players(self) -> List[int]:
        """The player numbers must be from 1 to the number specified"""
        return list(range(1, self.num_players + 1))

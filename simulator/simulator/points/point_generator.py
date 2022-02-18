import random
from typing import List
from constants import POINT_TO_SERVER, NUM_SERVES

class PointGenerator:
    def simulate_point(self, is_player_1_serve: bool) -> List[int]:
        ''' 
        Determines if the server wins the point
        The POINT_TO_SERVER determines how frequently the server wins
        '''
        random_number: float = random.random()
        does_server_win: bool = random_number <= POINT_TO_SERVER

        #
        # Player 1 can win if 
        #  player 1's serving and the server wins or 
        #  if player 1's not serving and the server loses
        #
        if (is_player_1_serve and does_server_win) or (not is_player_1_serve and not does_server_win):
            return [1, 0]

        return [0, 1]

    def simulate_num_serves(self) -> int:
        '''
        Determines randomly how many serves it took a player.
        The NUM_SERVES determines how frequently the server uses 1 serve. 
        '''
        random_number: float = random.random()
        if random_number <= NUM_SERVES:
            return 1

        return 2

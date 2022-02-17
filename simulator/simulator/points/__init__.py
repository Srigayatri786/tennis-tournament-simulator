import random
from constants import POINT_TO_SERVER

class PointGenerator:
    def simulate_point(self, is_player_1_serve) -> bool:
        """ 
        determines if the server wins the point
        """
        random_number = random.random()
        does_server_win = random_number <= POINT_TO_SERVER
        
        if (is_player_1_serve and does_server_win) or (not is_player_1_serve and not does_server_win):
            
            return [1, 0]
        else:
            return [0, 1]

    def simulate_num_serves(self) -> int:
        return random.randint(1,2)
from unittest import TestCase
from typing import List
from constants import POINT_TO_SERVER, NUM_SERVES
from simulator.points.point_generator import PointGenerator

class TestPointGenerator(TestCase):
    def setUp(self) -> None:
        self.point_generator_obj = PointGenerator()

    def test_point_to_one_player(self) -> None:
        '''
        Tests that only player gets a point
        '''
        point: List[int] = self.point_generator_obj.simulate_point(True)
        self.assertCountEqual(point, [0, 1])

    def test_player_1_server_randomness(self) -> None:
        '''
        Tests that whenn player 1 is the server, player 1 wins by the assigned percentage
        '''
        player_1_wins_count:int = 0
        total_count: int = 10000
        for _ in range(total_count):
            points: List[int] = self.point_generator_obj.simulate_point(True)
            player_1_wins_count += points[0]

        self.assertAlmostEqual(player_1_wins_count / total_count, POINT_TO_SERVER, 1)

    def test_player_2_server_randomness(self) -> None:
        '''
        Tests that whenn player 2 is the server, player 2 wins by the assigned percentage
        '''
        player_2_wins_count:int = 0
        total_count: int = 10000
        for _ in range(total_count):
            points: List[int] = self.point_generator_obj.simulate_point(False)
            player_2_wins_count += points[1]

        self.assertAlmostEqual(player_2_wins_count / total_count, POINT_TO_SERVER, 1)

    def test_num_serves_range(self)-> None:
        '''
        Tests that the num serves that is generated is in the range between 1 and 2
        '''
        num_serves:int = self.point_generator_obj.simulate_num_serves()
        self.assertTrue(1 <= num_serves <= 2)

    def test_num_serves_randomness(self) -> None:
        '''
        Tests that the number of serves randomness is in the range defined
        '''
        serve_1: int = 0
        total_count: int = 10000

        for _ in range(total_count):
            num_serves: int = self.point_generator_obj.simulate_num_serves()
            if num_serves == 1:
                serve_1 += 1

        self.assertAlmostEqual(serve_1 / total_count, NUM_SERVES, 1)

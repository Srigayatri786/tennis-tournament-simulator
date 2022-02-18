from typing import Union

GAME_TYPE = Union[int, str]

# defines the percentage of times the server will win the point
POINT_TO_SERVER = 0.6

# defines the percentage of times number of serves will be 1
NUM_SERVES  =  0.5

POINT_0 = 0
POINT_1 = 15
POINT_2 = 30
POINT_3 = 40
GAME_POINT = 'GAME'
DEUCE = 'DEUCE'
ADVANTAGE_POINT = 'AD'

GAME_POINTS = [POINT_0, POINT_1, POINT_2, POINT_3, GAME_POINT, DEUCE, ADVANTAGE_POINT]

NEXT_GAME_POINTS = {
    POINT_0: POINT_1,
    POINT_1: POINT_2,
    POINT_2: POINT_3,
    POINT_3: GAME_POINT,
    DEUCE: ADVANTAGE_POINT,
    ADVANTAGE_POINT: GAME_POINT
}

GAME_RECORD = {
    'round': 0,
    'player_1_num': 0,
    'player_2_num': 0,
    'player_1_point': 0,
    'player_2_point': 0,
    'player_1_game': 0,
    'player_2_game': 0,
    'player_1_set': 0,
    'player_2_set': 0,
    'player_1_match': 0,
    'player_2_match': 0,
    'is_player_1_server': 1,
    'num_serves': 0
}

# Tennis Tournament Simulator

This projects simulates a tennis tournament based on the rules mentioned [here](https://en.wikipedia.org/wiki/Tennis_scoring_system) and [here](https://www.youtube.com/watch?v=stdk_U0pL0o).

## Assumptions
- Players generated are ordered based on their strength from strong to weak.
- If a weak player beats a strong player, then the weak player is considered a strong player.
- Once in a tournament, there is no forfeiting allowed.
- A winner of match is determined by the person who wins best of 3 sets.
- The 1st player always serves first.
- Serve is changed when odd number of games have been played.
- Single elimination system is used

## Requirements:
- Python3
- pip
- venv

## Setup:
Run the setup.sh using the following command:
```
sh setup.sh
```

## Activate the environment
```
cd simulator/
source venv/bin/activate
```

## Running the simulator
```
python3 ./simulator/ --num_players NUM_PLAYERS --logs LOG_FILE_STORED
```

- num_players: The number of players to play the tournament. By default, 64 players are assumed. It must be between 2 and 64.
- logs: The place where logs should be stored. By default, it stores it in the logs folder. The logs are stored as a csv.

## Testing
```
cd simulator/
python3 -m unittest discover -v
```
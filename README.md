# tennis-tournament-simulator

This projects simulates a tennis tournament based on the rules mentioned here. In addition, the following assumptions have been made:

- Players generated are ordered based on their strength from strong to weak.
- If a weak player beats a strong player, then the weak player is considered a strong player
- Once in a tournament, there is no forfeiting allowed
- A winner of match is determined by the person who wins best of 3 sets.
- The 1st player always serves first.
- Serve is changed whenn odd number of games have been played.

Requirements:
- Python3
- pip
- venv

Setup:
Run the setup.sh using the following command:

Running the simulator:

- python3 ./simulator/
  - --num_players: The number of players to play the tournament. It must be between 2 and 64.
  - --logs: The place where logs should be stored. By default, it stores it in the logs folder. The logs are stored as a csv.

Testing:
python3 -m unittest discover -v
can be used to runn the testcases for the simulator.
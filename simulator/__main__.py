import argparse
from simulator.simulator import Simulator
from simulator.save_logs.save_logs_csv import SaveLogsAsCSV

parser = argparse.ArgumentParser(description='Parse arguments for the tennis simulator')
num_players_argument = parser.add_argument(
    '--num_players',
    dest='num_players',
    help='enter number of players (default  64)',
    default=64,
    type=int
)
logs_argument = parser.add_argument(
    '--logs',
    dest='logs',
    help='where should the logs be saved',
    default='../logs/',
    type=str
)

args = parser.parse_args()
if __name__ == '__main__':
    try:
        if args.num_players > 64 or args.num_players < 2:
            raise argparse.ArgumentError(num_players_argument, "Number of players should be between 2 and 64 (inclusive).")
        
        simulator = Simulator(args.num_players)
        simulator.simulate_tennis_tournament()

        winner = simulator.get_winner()
        logs = simulator.get_logs()

        save_to_csv = SaveLogsAsCSV(args.logs)
        save_to_csv.save_logs(logs)

    except argparse.ArgumentError as err:
        print(err)

from simulator.points.point_generator import PointGenerator
from simulator.games.game_scorer import GameScorer
from simulator.sets.set_scorer import SetScorer
from simulator.matches.best_of_3_match_scorer import BestOfThreeMatchScorer
from simulator.game_record import GameRecord

class MatchSimulator:
    def __init__(self, round, player_1, player_2):
        self.round = round
        self.player_1 = player_1
        self.player_2 = player_2

        self.point_simulator =  PointGenerator()
        self.game_scorer = GameScorer()
        self.set_scorer = SetScorer()
        self.match_scorer = BestOfThreeMatchScorer()
        self.game_record = GameRecord(self.round, self.player_1, self.player_2)
        self.match_logs = []
        self.winner = -1

    def simulate_match(self):
        while self.match_scorer.get_match_winner(self.game_record.get_match_scores()) == -1:
            points = self.point_simulator.simulate_point(self.game_record.get_server_information())
            num_serves = self.point_simulator.simulate_num_serves()

            self.game_record.update_points(points)
            self.game_record.update_num_serves(num_serves)

            game_scores = self.game_scorer.get_game_point(points, self.game_record.get_game_scores())
            game_winner = self.game_scorer.player_game_point(game_scores)

            if game_winner >= 0:

                # update the set scores
                set_scores = self.set_scorer.get_set_scores(self.game_record.get_set_scores(), game_winner)

                # update the game scores
                game_scores = [0, 0]

                # get set winner
                set_winner = self.set_scorer.get_set_winner(set_scores)
                if set_winner >= 0:
                    match_scores = self.match_scorer.score_match(self.game_record.get_match_scores(), set_winner)

                    set_scores = [0, 0]
                    self.game_record.update_match_scores(match_scores)
                    
                # get the player to serve
                is_player_1_server = self.set_scorer.is_player_1_serve(set_scores)
                self.game_record.update_set_score(set_scores)
                self.game_record.update_server_information(is_player_1_server)
            
            self.game_record.update_game_score(game_scores)
            self.match_logs.append(self.game_record.get_game_record_information())
        self.winner = self.match_scorer.get_match_winner(self.game_record.get_match_scores())

    def get_winner(self):
        if self.winner == -1:
            return -1
        if self.winner == 0:
            return self.player_1
        return self.player_2
    
    def get_match_logs(self):
        return self.match_logs


        
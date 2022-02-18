from typing import List
from constants import GAME_TYPE
from simulator.points.point_generator import PointGenerator
from simulator.games.game_scorer import GameScorer
from simulator.sets.set_scorer import SetScorer
from simulator.matches.best_of_3_match_scorer import BestOfThreeMatchScorer
from simulator.game_record import GameRecord

class MatchSimulator:
    """Simulates a match between 2 players"""

    def __init__(self, round_num: int, player_1: int, player_2: int) -> None:
        """Initializes tthe classes required"""
        self.round: int = round_num
        self.player_1: int = player_1
        self.player_2: int = player_2

        self.point_simulator: PointGenerator =  PointGenerator()
        self.game_scorer: GameScorer = GameScorer()
        self.set_scorer: SetScorer = SetScorer()
        self.match_scorer: BestOfThreeMatchScorer = BestOfThreeMatchScorer()
        self.game_record: GameRecord = GameRecord(self.round, self.player_1, self.player_2)
        self.match_logs: List[List[GAME_TYPE]] = []
        self.winner: int = -1

    def get_updated_game_scores(self) -> None:
        """Simulates the point and gets the updated game score"""
        # simulate a point
        points: List[int] = self.point_simulator.simulate_point(self.game_record.get_server_information())

        # simulate number of serves
        num_serves: int = self.point_simulator.simulate_num_serves()

        # update the game record with the necessary information
        self.game_record.update_points(points)
        self.game_record.update_num_serves(num_serves)

        # compute the game scores and game winner
        game_scores: List[GAME_TYPE] = self.game_scorer.get_game_point(points, self.game_record.get_game_scores())
        game_winner: int = self.game_scorer.player_game_point(game_scores)

        if game_winner >= 0:
            game_scores = [0, 0]

        self.game_record.update_game_score(game_scores)
        return game_winner

    def get_updated_set_score(self, game_winner: int) -> None:
        """If there is a game winner, update the set score"""
        # computes the set scores and winners
        set_scores: List[int] = self.set_scorer.get_set_scores(self.game_record.get_set_scores(), game_winner)
        set_winner: int = self.set_scorer.get_set_winner(set_scores, self.game_record.get_set_scores())

        if set_winner >= 0:
            set_scores = [0, 0]

        # updates the player serving information
        self.get_server_information(set_scores)
        self.game_record.update_set_score(set_scores)

        return set_winner

    def get_server_information(self, set_scores: List[int]) -> None:
        """Update the player who will be serving based on the new set scores"""
        is_player_1_server: bool = self.set_scorer.is_player_1_serving(
            set_scores, 
            self.game_record.get_server_information()
        )
        self.game_record.update_server_information(is_player_1_server)

    def get_match_information(self, set_winner) -> None:
        """Updates the match scores based on the winner of the set scores."""
        match_scores: List[int] = self.match_scorer.score_match(
            self.game_record.get_match_scores(), 
            set_winner
        )

        self.game_record.update_match_scores(match_scores)

    def simulate_match(self) -> int:
        """Simulates the match and returns the winner"""
        while self.match_scorer.get_match_winner(self.game_record.get_match_scores()) == -1:
            game_winner = self.get_updated_game_scores()

            set_winner = -1
            if game_winner >= 0:
                set_winner = self.get_updated_set_score(game_winner)

            if set_winner >= 0:
                self.get_match_information(set_winner)

            # update match logs
            self.match_logs.append(self.game_record.get_game_record_information())

        # get the winner of the game
        winner = self.match_scorer.get_match_winner(self.game_record.get_match_scores())
        return self._get_winner(winner)

    def _get_winner(self, winner: int) -> int:
        """Takes the index of the player and returns the player num."""
        if winner == -1:
            return -1
        if winner == 0:
            return self.player_1
        return self.player_2

    def get_match_logs(self) -> List[List[GAME_TYPE]]:
        """Gets the match logs"""
        return self.match_logs




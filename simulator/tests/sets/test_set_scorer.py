from unittest import TestCase
from typing import List
from simulator.sets.set_scorer import SetScorer

class TestSetScorer(TestCase):
    def setUp(self) -> None:
        self.set_scorer_obj: SetScorer = SetScorer()

    
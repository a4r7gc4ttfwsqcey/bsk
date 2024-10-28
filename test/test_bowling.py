import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_init_game(self):
        game = BowlingGame()
        self.assertTrue(isinstance(game._frames, list))

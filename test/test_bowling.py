import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_init_game(self):
        game = BowlingGame()
        self.assertTrue(isinstance(game._frames, list))

    def test_add_single_frame(self):
        frame = Frame(1, 5)
        game = BowlingGame()
        game.add_frame(frame)
        self.assertEqual(1, len(game._frames))
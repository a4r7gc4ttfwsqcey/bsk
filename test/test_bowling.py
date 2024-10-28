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

    def test_get_single_frame(self):
        frame = Frame(1, 5)
        game = BowlingGame()
        game.add_frame(frame)
        self.assertEqual(frame, game.get_frame_at(0))

    def test_add_get_10_frames(self):
        frames = [
            [1, 5],
            [3, 6],
            [7, 2],
            [3, 6],
            [4, 4],
            [5, 3],
            [3, 3],
            [4, 5],
            [8, 1],
            [2, 6]
        ]
        game = BowlingGame()
        for idx, value in enumerate(frames):
            frame = Frame(value[0], value[1])
            game.add_frame(frame)
            self.assertEqual(frame, game.get_frame_at(idx))
import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):
    _test_frames: list[list[int]] = [
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
        game = BowlingGame()
        for idx, value in enumerate(self._test_frames):
            frame = Frame(value[0], value[1])
            game.add_frame(frame)
            self.assertEqual(frame, game.get_frame_at(idx))

    def test_add_frame_full(self):
        game = BowlingGame()
        for count in range(0, 10):
            game.add_frame(Frame(0, 0))
        with self.assertRaises(BowlingError):
            game.add_frame(Frame(1, 1))

    def test_get_frame_not_exist(self):
        game = BowlingGame()
        with self.assertRaises(BowlingError):
            game.get_frame_at(0)

    def test_calculate_score(self):
        game = BowlingGame()
        for value in self._test_frames:
            frame = Frame(value[0], value[1])
            game.add_frame(frame)
        self.assertEqual(81, game.calculate_score())

    def test_calculate_score_spare(self):
        game = BowlingGame()
        for value in [[1, 9]] + self._test_frames[1:]:
            frame = Frame(value[0], value[1])
            game.add_frame(frame)
        self.assertEqual(88, game.calculate_score())

    def test_calculate_score_strike(self):
        game = BowlingGame()
        for value in [[10, 0]] + self._test_frames[1:]:
            frame = Frame(value[0], value[1])
            game.add_frame(frame)
        self.assertEqual(94, game.calculate_score())

    def test_calculate_score_strike_and_spare(self):
        game = BowlingGame()
        for value in [[10, 0], [4, 6]] + self._test_frames[2:]:
            frame = Frame(value[0], value[1])
            game.add_frame(frame)
        self.assertEqual(103, game.calculate_score())

    def test_calculate_score_two_strikes(self):
        game = BowlingGame()
        for value in [[10, 0], [10, 0]] + self._test_frames[2:]:
            frame = Frame(value[0], value[1])
            game.add_frame(frame)
        self.assertEqual(112, game.calculate_score())

    def test_calculate_score_two_spares(self):
        game = BowlingGame()
        for value in [[8, 2], [5, 5]] + self._test_frames[2:]:
            frame = Frame(value[0], value[1])
            game.add_frame(frame)
        self.assertEqual(98, game.calculate_score())

    def test_calculate_score_spare_as_last(self):
        game = BowlingGame()
        for value in [[1, 5]] + self._test_frames[1:-1] + [[2, 8]]:
            frame = Frame(value[0], value[1])
            game.add_frame(frame)
        game.set_first_bonus_throw(7)
        self.assertEqual(90, game.calculate_score())

    def test_calculate_score_strike_as_last(self):
        game = BowlingGame()
        for value in [[1, 5]] + self._test_frames[1:-1] + [[10, 0]]:
            frame = Frame(value[0], value[1])
            game.add_frame(frame)
        game.set_first_bonus_throw(7)
        game.set_second_bonus_throw(2)
        self.assertEqual(92, game.calculate_score())

    def test_calculate_score_perfect_game(self):
        game = BowlingGame()
        num = 10
        while num:
            game.add_frame(Frame(10, 0))
            num -= 1
        game.set_first_bonus_throw(10)
        self.assertEqual(300, game.calculate_score())

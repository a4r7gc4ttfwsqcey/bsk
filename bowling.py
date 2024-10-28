from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self._frames: list[Frame] = []
        self._bonus_throw: int = 0
        self._second_bonus_throw: int = 0
    
    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) > 9:
            raise BowlingError("10 frames is the maximum for the game.")
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        try:
            return self._frames[i]
        except Exception:
            raise BowlingError("Index out of range")

    def calculate_score(self) -> int:
        try:
            total_score: int = 0
            for idx, frame in enumerate(self._frames):
                if frame.is_strike() is True:
                    if idx == len(self._frames) - 1:
                        total_score += self._bonus_throw + self._second_bonus_throw
                    else:
                        if self._frames[idx + 1].is_strike():
                            if idx == len(self._frames) - 2:
                                total_score += self._bonus_throw + self._frames[idx + 1].get_first_throw()
                            else:
                                total_score += self._frames[idx + 2].get_first_throw()
                        total_score += self._frames[idx + 1].get_first_throw() + self._frames[idx + 1].get_second_throw()
                elif frame.is_spare() is True:
                    if idx != len(self._frames) - 1:
                        total_score += self._frames[idx + 1].get_first_throw()
                    else:
                        total_score += self._bonus_throw
                total_score += frame.score()
            return total_score
        except Exception:
            raise BowlingError("Unable to calculate total score.")

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self._bonus_throw = bonus_throw

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        self._second_bonus_throw = bonus_throw

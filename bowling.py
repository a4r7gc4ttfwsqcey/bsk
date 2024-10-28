from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self._frames: list[Frame] = []
    
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
        total_score: int = 0
        spare: bool = False
        strike: bool = False
        for frame in self._frames:
            if strike is True:
                total_score += frame.get_first_throw() + frame.get_second_throw()
                strike = False
            elif spare is True:
                total_score += frame.get_first_throw()
                spare = False
            total_score += frame.score()
            if frame.is_strike():
                strike = True
            elif frame.is_spare():
                spare = True
        return total_score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass

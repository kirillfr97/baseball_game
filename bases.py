from random import randint


class Bases:
    def __init__(self):
        self._bases: int = 0b000
        self._scored_runs: int = 0

    def score(self) -> int:
        return self._scored_runs

    def advance_bases(self, number_to_advance: int) -> int:
        self._bases = self._bases << number_to_advance | 1 << (number_to_advance - 1)
        result = (self._bases >> 3).bit_count()
        self._scored_runs += result
        self._bases &= 0b0111
        return result

    @staticmethod
    def calculate_new_runs() -> int:
        return randint(1, 8)

    def restart(self):
        self._bases = 0b000
        self._scored_runs = 0
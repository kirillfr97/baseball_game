from typing import List
from random import randint


class Bases:
    def __init__(self):
        self._bases: List[int] = [0, 0, 0]
        self._scored_runs: int = 0

    def score(self) -> int:
        return self._scored_runs

    def advance_bases(self, number_to_advance: int) -> int:
        result = 0
        if number_to_advance == 4:
            result += sum(self._bases) + 1
            self._bases = [0, 0, 0]
        else:
            for _ in range(number_to_advance):
                result += self._bases.pop()
                self._bases.append(0)
            self._bases[number_to_advance - 1] = 1
        self._scored_runs += result
        return result

    @staticmethod
    def calculate_new_runs() -> int:
        return randint(1, 8)

    def restart(self):
        self._bases = [0, 0, 0]
        self._scored_runs = 0
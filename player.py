class Player:
    def __init__(self, name: str):
        self._player_name: str = name
        self._score: int = 0

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, score: int):
        self._score = score

    @property
    def name(self) -> str:
        return self._player_name

    @name.setter
    def name(self, name: str):
        self._player_name = name

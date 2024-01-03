import enum
from abc import ABC, abstractmethod
from dataclasses import dataclass

from models.user import User


@dataclass
class Stats:
    wins: int = 0
    losses: int = 0
    draws: int = 0
    games: int = 0


class Actor(ABC):

    @abstractmethod
    def play(self):
        pass


class Player(Actor):

    def __init__(self, user: User, mark=None, ):
        self.user = user
        self.mark = mark

    @property
    def stats(self):
        return Stats(
            losses=self.user.losses,
            wins=self.user.wins,
            draws=self.user.draw,
            games=self.user.played_games
        )

    def play(self) -> dict[str, str]:
        position = input(f"{self.user.username} Position:\n ")
        return {
            "position": position.strip().capitalize(),
            "mark": self.mark
        }

    def add_points(self):
        self.user.points += 1
        pass

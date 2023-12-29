import enum
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Stats:
    wins: int = 0
    losses: int = 0
    draws: int = 0
    games: int = 0


@dataclass
class Profile:
    name: str
    stats: Stats = Stats()
    points: int = 0


class Mark(enum.Enum):
    X: str = "X"
    O: str = "O"


class Actor(ABC):

    @abstractmethod
    def play(self, position):
        pass


class Player(Actor, Profile):

    def __init__(self, mark: Mark, profile:Profile):
        self.mark: Mark = mark

    def play(self, position) -> bool():
        pass

    def add_points(self):
        pass


class User(Profile):

    def __init__(self):
        self.profile = None

    def setprofile(self, profile: Profile):
        self.profile = profile

    def register_user(self, profile: Profile, password):
        self.profile = profile
        pass

    def update(self, data):
        pass

    def get_user(self, username, password):
        pass

    def get_users(self) -> list[Profile]:
        pass

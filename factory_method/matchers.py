from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def run(self) -> str:
        matcher = self.factory_method()
        return matcher.match()


class Matcher(ABC):

    @abstractmethod
    def match(self) -> str:
        pass


def get_matcher(creator: Creator) -> None:

    print(creator.run())

from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class ClubeMatcher(Command):

    def execute(self):
        return "clube matcher"


class DefaultMatcher(Command):

    def execute(self):
        return "default matcher"
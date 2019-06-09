from __future__ import annotations
from abc import abstractmethod, ABC
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    def detach(self, observer: Observer) -> None:
        pass

    def notify(self) -> None:
        pass


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

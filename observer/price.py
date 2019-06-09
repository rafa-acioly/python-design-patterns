from typing import Dict, List, Optional
from base import Subject, Observer
from random import randrange


class PriceSubject(Subject):

    _instance = None
    _state: List[Dict] = []
    _observers: List[Observer] = []

    @staticmethod
    def instance():
        if PriceSubject._instance is None:
            PriceSubject._instance = PriceSubject()
        return PriceSubject._instance

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def apply_price(self):
        self._state = [{'key': randrange(1, 5)}]
        self.notify()

from base import Observer, Subject


class RedisPriceObserver(Observer):

    def update(self, subject: Subject) -> None:
        if not len(subject._state) == 0:
            print("Cache data stored")

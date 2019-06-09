from base import Subject, Observer


class PriceLakeObserver(Observer):

    def update(self, subject: Subject) -> None:
        if not len(subject._state) == 0:
            print("Data sended to datalake")

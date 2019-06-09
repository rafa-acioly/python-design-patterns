from price import PriceSubject
from redis import RedisPriceObserver
from lake import PriceLakeObserver


def run():
    price_subject = PriceSubject.instance()

    redis_observer = RedisPriceObserver()
    price_subject.attach(redis_observer)

    price_subject.apply_price()

    another_method()


def another_method():
    price_subject = PriceSubject.instance()

    lake_observer = PriceLakeObserver()
    price_subject.attach(lake_observer)

    price_subject.apply_price()


if __name__ == "__main__":
    run()

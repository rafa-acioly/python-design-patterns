from price import PriceSubject
from redis import RedisPriceObserver
from lake import PriceLakeObserver


def run():
    price_subject = PriceSubject()

    redis_observer = RedisPriceObserver()
    price_subject.attach(redis_observer)

    lake_observer = PriceLakeObserver()
    price_subject.attach(lake_observer)

    price_subject.apply_price()

    price_subject.detach(lake_observer)

    price_subject.apply_price()


if __name__ == "__main__":
    run()

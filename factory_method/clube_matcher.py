from matchers import Matcher, Creator


class ConcreteClubeMatcher(Matcher):

    def match(self) -> str:
        return "from ConcreteClubeMatcher"


class ConcreteClubeCreator(Creator):

    def factory_method(self) -> ConcreteClubeMatcher:
        return ConcreteClubeMatcher()

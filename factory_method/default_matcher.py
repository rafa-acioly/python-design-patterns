from matchers import Matcher, Creator


class ConcreteDefaultMatcher(Matcher):

    def match(self) -> str:
        return "from ConcreteDefaultMatcher"


class ConcreteDefaultCreator(Creator):

    def factory_method(self) -> ConcreteDefaultMatcher:
        return ConcreteDefaultMatcher()

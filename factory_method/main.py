from clube_matcher import ConcreteClubeCreator
from default_matcher import ConcreteDefaultCreator
from matchers import get_matcher


if __name__ == "__main__":
    get_matcher(ConcreteClubeCreator())
    get_matcher(ConcreteDefaultCreator())

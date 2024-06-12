import dataclasses
from abc import abstractmethod, ABC
from collections import defaultdict

from frozendict import frozendict


# noinspection PyUnusedLocal
# skus = unicode string


@dataclasses.dataclass(frozen=True)
class State:
    current_cost: int
    unprocessed_basket: frozendict[str, int]


class Offer(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def apply(self, state: State) -> State:
        ...


@dataclasses.dataclass(frozen=True)
class NOffer(Offer):
    N: int
    letter: str
    for_: int

    def apply(self, state: State) -> State:
        items = state.unprocessed_basket.get(self.letter, 0)
        price = items // self.N * self.for_

        basket = state.unprocessed_basket.set(self.letter, items % self.N)
        return State(current_cost=state.current_cost + price, unprocessed_basket=basket)


@dataclasses.dataclass(frozen=True)
class FreeOffer(Offer):
    N: int
    buy_letter: str
    get_free_letter: str

    def apply(self, state: State) -> State:
        buy_items = state.unprocessed_basket.get(self.buy_letter, 0)
        get_free_items = state.unprocessed_basket.get(self.get_free_letter, 0)

        free_items = buy_items // self.N
        basket = state.unprocessed_basket.set(self.get_free_letter, max(0, get_free_items - free_items))
        return State(current_cost=state.current_cost, unprocessed_basket=basket)


@dataclasses.dataclass(frozen=True)
class JustOffer(Offer):
    letter: str
    price: int

    def apply(self, state: State) -> State:
        return State(current_cost=state.current_cost + self.price * state.unprocessed_basket.get(self.letter, 0),
                     unprocessed_basket=state.unprocessed_basket.set(self.letter, 0))


offers = [
    FreeOffer(N=2, buy_letter="E", get_free_letter="B"),
    FreeOffer(N=2, buy_letter="F", get_free_letter="F"),


    NOffer(N=5, letter="A", for_=200),
    NOffer(N=3, letter="A", for_=130),
    NOffer(N=2, letter="B", for_=45),
    NOffer(N=10, letter="H", for_=80),



    JustOffer(letter="A", price=50),
    JustOffer(letter="B", price=30),
    JustOffer(letter="C", price=20),
    JustOffer(letter="D", price=15),
    JustOffer(letter="E", price=40),
    JustOffer(letter="F", price=10),
    JustOffer(letter="G", price=20),
    JustOffer(letter="H", price=10),
    JustOffer(letter="I", price=35),
    JustOffer(letter="J", price=60),
    JustOffer(letter="K", price=80),
    JustOffer(letter="L", price=90),
    JustOffer(letter="M", price=15),
    JustOffer(letter="N", price=40),
    JustOffer(letter="O", price=10),
    JustOffer(letter="P", price=50),
    JustOffer(letter="Q", price=30),
    JustOffer(letter="R", price=50),
    JustOffer(letter="S", price=30),
    JustOffer(letter="T", price=20),
    JustOffer(letter="U", price=40),
    JustOffer(letter="V", price=50),
    JustOffer(letter="W", price=20),
    JustOffer(letter="X", price=90),
    JustOffer(letter="Y", price=10),
    JustOffer(letter="Z", price=50),

]


def get_total(basket: dict[str, int]) -> int:
    A = basket.get("A", 0)
    B = basket.get("B", 0)
    C = basket.get("C", 0)
    D = basket.get("D", 0)
    E = basket.get("E", 0)
    F = basket.get("F", 0)

    total = 0
    total += A // 5 * 200
    total += (A % 5) // 3 * 130
    total += (A % 5) % 3 * 50

    B = max(0, B - E // 2)
    total += (B // 2) * 45 + (B % 2) * 30

    total += C * 20
    total += D * 15
    total += E * 40

    total += ((F // 3) * 2 + (F % 3)) * 10

    return total


def checkout(skus: str) -> int:
    skus = skus.replace(' ', '')  # don't know the format yet
    counts: dict[str, int] = defaultdict(int)

    for s in skus:
        if s in "ABCDEF":
            counts[s] += 1
        else:
            return -1

    return get_total(counts)

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

        if self.buy_letter != self.get_free_letter:
            free_items = buy_items // self.N
            basket = state.unprocessed_basket.set(self.get_free_letter, max(0, get_free_items - free_items))
            return State(current_cost=state.current_cost, unprocessed_basket=basket)

        basket = state.unprocessed_basket.set(self.get_free_letter,
                                              buy_items // (self.N + 1) * self.N + buy_items % (self.N + 1))
        return State(current_cost=state.current_cost, unprocessed_basket=basket)


@dataclasses.dataclass(frozen=True)
class AnyOffer(Offer):
    letters: str
    price: int
    N: int

    def apply(self, state: State) -> State:
        total_items = sum([state.unprocessed_basket.get(l, 0) for l in self.letters])
        num_offers = total_items // self.N

        remaining_items = self.N * num_offers
        basket = state.unprocessed_basket
        for letter in self.letters:
            value = basket.get(letter, 0)
            new_value = max(0, value - remaining_items)

            remaining_items -= value - new_value
            basket = basket.set(letter, new_value)

            if remaining_items == 0:
                break

        assert remaining_items == 0

        return State(current_cost=state.current_cost + self.price * num_offers, unprocessed_basket=basket)


@dataclasses.dataclass(frozen=True)
class JustOffer(Offer):
    letter: str
    price: int

    def apply(self, state: State) -> State:
        return State(current_cost=state.current_cost + self.price * state.unprocessed_basket.get(self.letter, 0),
                     unprocessed_basket=state.unprocessed_basket.set(self.letter, 0))


offers = [
    AnyOffer(letters="ZYSTX", N=3, price=45),  # cheapest has to go latest

    FreeOffer(N=2, buy_letter="E", get_free_letter="B"),
    FreeOffer(N=2, buy_letter="F", get_free_letter="F"),
    FreeOffer(N=3, buy_letter="N", get_free_letter="M"),
    FreeOffer(N=3, buy_letter="R", get_free_letter="Q"),
    FreeOffer(N=3, buy_letter="U", get_free_letter="U"),

    NOffer(N=5, letter="A", for_=200),
    NOffer(N=3, letter="A", for_=130),
    NOffer(N=2, letter="B", for_=45),
    NOffer(N=10, letter="H", for_=80),
    NOffer(N=5, letter="H", for_=45),
    NOffer(N=2, letter="K", for_=120),
    NOffer(N=5, letter="P", for_=200),
    NOffer(N=3, letter="Q", for_=80),
    NOffer(N=3, letter="V", for_=130),
    NOffer(N=2, letter="V", for_=90),

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
    JustOffer(letter="K", price=70),
    JustOffer(letter="L", price=90),
    JustOffer(letter="M", price=15),
    JustOffer(letter="N", price=40),
    JustOffer(letter="O", price=10),
    JustOffer(letter="P", price=50),
    JustOffer(letter="Q", price=30),
    JustOffer(letter="R", price=50),
    JustOffer(letter="S", price=20),
    JustOffer(letter="T", price=20),
    JustOffer(letter="U", price=40),
    JustOffer(letter="V", price=50),
    JustOffer(letter="W", price=20),
    JustOffer(letter="X", price=17),
    JustOffer(letter="Y", price=20),
    JustOffer(letter="Z", price=21),

]


def get_total(basket: dict[str, int]) -> int:
    state = State(current_cost=0, unprocessed_basket=frozendict(basket))
    for offer in offers:
        state = offer.apply(state)

    assert max(state.unprocessed_basket.values()) == 0
    return state.current_cost


def checkout(skus: str) -> int:
    skus = skus.replace(' ', '')  # don't know the format yet
    counts: dict[str, int] = defaultdict(int)

    for s in skus:
        if s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            counts[s] += 1
        else:
            return -1

    return get_total(counts)




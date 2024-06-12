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



class NOffer:
    @abstractmethod
    @property
    def N(self) -> int:
        ...

    @abstractmethod
    @property
    def letter(self) -> str:
        ...


    @abstractmethod
    @property
    def for_(self):
        ...

    def apply(self, state: State) -> State:
        price = state.unprocessed_basket.get(self.letter, 0) // self.N * self.for_

        basked = st







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

    total += ((F // 3) * 2 +(F % 3) ) * 10

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




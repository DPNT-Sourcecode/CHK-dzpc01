from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string


def get_total(basket: dict[str, int]) -> int:
    print(basket)
    A = basket.get("A", 0)
    B = basket.get("B", 0)
    C = basket.get("C", 0)
    D = basket.get("D", 0)
    E = basket.get("E", 0)

    total = 0
    total += A // 5 * 200
    total += (A % 5) // 3 * 130
    total += (A % 5) % 3 * 50

    B = max(0, B - E // 2)
    total += (B // 2) * 45 + (B % 2) * 30

    total += C * 20
    total += D * 15
    total += E * 40

    print(A, B, C, D, E)

    return total


def checkout(skus: str) -> int:
    skus = skus.replace(' ', '')  # don't know the format yet
    counts: dict[str, int] = defaultdict(int)

    for s in skus:
        if s in "ABCDE":
            counts[s] += 1
        else:
            return -1

    return get_total(counts)





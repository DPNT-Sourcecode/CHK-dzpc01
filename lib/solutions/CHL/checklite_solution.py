from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string


def get_total(basket: dict[str, int]) -> int:
    return (basket.get("A", 0) // 3 * 130 + basket.get("A", 0) % 3 * 50 +
            basket.get("B", 0) // 2 * 45 + basket.get("B", 0) % 2 * 30 +
            basket.get("C", 0) * 20 + basket.get("D", 0) * 15)


def checklite(skus: str) -> int:
    skus = skus.upper().replace(' ', '')  # don't know the format yet
    counts: dict[str, int] = defaultdict(int)

    for s in skus:
        if s in "ABCD":
            counts[s] += 1
        else:
            return -1

    return get_total(counts)



from unittest import TestCase

from frozendict import frozendict
from solutions.CHK import checkout_solution


class TestCheckout(TestCase):
    def test_incorrect(self):
        assert checkout_solution.checkout("ABCDEFGH") == -1

    def test_discounts(self):
        assert checkout_solution.checkout("AAAAAAAAABBBCCD") == 510
        # AAAAA+AAA+A = 200 + 130 + 50 = 380
        # BB+B = 45 + 30 = 75
        # CC = 20 * 2 = 40
        # D = 15 * 1 = 15
        # 380 + 75 + 40 + 15 = 510

    def test_e_disables_b(self):
        assert checkout_solution.checkout("AAAABBBBCCDEE") == 390
        # AAA+A = 130 + 50 = 180
        # BBB+B-BB = 45 + 30 = 75
        # CC = 20 * 2 = 40
        # D = 15 * 1 = 15
        # EE = 40 * 2 = 80
        # 180 + 75 + 40 + 80 = 390

    def test_format(self):
        assert checkout_solution.checkout("a b") == -1

    def test_empty(self):
        assert checkout_solution.checkout("") == 0

    def test_f(self):
        assert checkout_solution.checkout("FFFFFFFF") == 60
        # FF[F] FF[F] FF, where [F] is a free item


class TestNOffer(TestCase):
    def test_apply(self):
        state = checkout_solution.State(current_cost=0, unprocessed_basket=frozendict({"A": 12, "B": 20}))
        offer = checkout_solution.NOffer(N=5, letter="A", for_=200)
        new_state = offer.apply(state)

        assert new_state.current_cost == 400
        assert new_state.unprocessed_basket == {"A": 2, "B": 20}



from unittest import TestCase

from frozendict import frozendict
from solutions.CHK import checkout_solution


class TestCheckout(TestCase):
    def test_incorrect(self):
        assert checkout_solution.checkout("ABCDEFGHЯ") == -1

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

    def test_g(self):
        assert checkout_solution.checkout("G") == 20

    def test_k(self):
        assert checkout_solution.checkout("K") == 70



class TestNOffer(TestCase):
    def test_apply(self):
        state = checkout_solution.State(current_cost=0, unprocessed_basket=frozendict({"A": 12, "B": 20}))
        offer = checkout_solution.NOffer(N=5, letter="A", for_=200)
        new_state = offer.apply(state)

        assert new_state.current_cost == 400
        assert new_state.unprocessed_basket == {"A": 2, "B": 20}


class TestFreeOffer(TestCase):
    def test_apply(self):
        state = checkout_solution.State(current_cost=0, unprocessed_basket=frozendict({"A": 12, "B": 20}))
        offer = checkout_solution.FreeOffer(N=5, buy_letter="A", get_free_letter="B")
        new_state = offer.apply(state)
        assert new_state.current_cost == 0
        assert new_state.unprocessed_basket == {"A": 12, "B": 18}


class TestJustOffer(TestCase):
    def test_apply(self):
        state = checkout_solution.State(current_cost=0, unprocessed_basket=frozendict({"A": 3, "B": 20}))
        offer = checkout_solution.JustOffer(letter="A", price=200)
        new_state = offer.apply(state)
        assert new_state.current_cost == 600
        assert new_state.unprocessed_basket == {"A": 0, "B": 20}


class TestAnyOffer(TestCase):
    def test_apply(self):
        state = checkout_solution.State(current_cost=0, unprocessed_basket=frozendict({"A": 9, "B": 7, "C": 3, "D": 2}))
        offer = checkout_solution.AnyOffer(letters="ABC", N=3, price=1)
        new_state = offer.apply(state)
        assert new_state.current_cost == 6
        assert new_state.unprocessed_basket == {"A": 0, "B": 0, "C": 1, "D": 2}

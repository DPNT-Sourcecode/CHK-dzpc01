from unittest import TestCase

from solutions.CHK import checkout_solution


class TestCheckout(TestCase):
    def test_incorrect(self):
        assert checkout_solution.checkout("ABCDE") == -1

    def test_discounts(self):
        assert checkout_solution.checkout("AAAABBBCCD") == 310
        # AAA+A = 130 + 50 = 180
        # BB+B = 45 + 30 = 75
        # CC = 20 * 2 = 40
        # D = 15 * 1 = 15
        # 180 + 75 + 40 + 15 = 310

    def test_format(self):
        assert checkout_solution.checkout("a b") == -1

    def test_empty(self):
        assert checkout_solution.checkout("") == 0



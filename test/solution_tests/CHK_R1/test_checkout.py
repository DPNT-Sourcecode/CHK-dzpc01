from unittest import TestCase

from solutions.CHL import checklite_solution


class TestCheckout(TestCase):
    def test_incorrect(self):
        assert checklite_solution.checklite("ABCDE") == -1

    def test_discounts(self):
        assert checklite_solution.checklite("AAAABBBCCD") == 310
        # AAA+A = 130 + 50 = 180
        # BB+B = 45 + 30 = 75
        # CC = 20 * 2 = 40
        # D = 15 * 1 = 15
        # 180 + 75 + 40 + 15 = 310


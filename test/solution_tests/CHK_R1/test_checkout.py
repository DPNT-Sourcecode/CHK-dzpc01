from unittest import TestCase

from solutions.CHK import checkout_solution


class TestCheckout(TestCase):
    def test_incorrect(self):
        assert checkout_solution.checkout("ABCDE") == -1

    def test_discounts(self):
        assert checkout_solution.checkout("AAAAAAAAABBBCCD") == 510
        # AAAAA+AAA+A = 200+130 + 50 = 180
        # BB+B = 45 + 30 = 75
        # CC = 20 * 2 = 40
        # D = 15 * 1 = 15
        # 200+180 + 75 + 40 + 15 = 510


    def test_e_disables_b(self):
        assert checkout_solution.checkout("AAAABBBBBCCDEE") == 390
        # AAA+A = 130 + 50 = 180
        # BBBB+B-BB = 45 + 30 = 75
        # CC = 20 * 2 = 40
        # D = 15 * 1 = 15
        # EE = 40 * 2 = 80
        # 180 + 75 + 40 + 15 + 80 = 390


    def test_format(self):
        assert checkout_solution.checkout("a b") == -1

    def test_empty(self):
        assert checkout_solution.checkout("") == 0




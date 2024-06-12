from unittest import TestCase

from solutions.CHL import checklite_solution

class TestCheckout(TestCase):
    def test_incorrect(self):
        assert checklite_solution.compute("ABCDE") == -1


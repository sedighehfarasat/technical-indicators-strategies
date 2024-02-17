import random
from strategies.rsi_cross_over import rsi_middle_line_cross_over
from unittest import TestCase


class Test(TestCase):
    def test_rsi_middle_line_cross_over(self):
        adj_prices = random.sample(range(1200, 3400), 400)
        period = 13
        buy_signals, sell_signals = rsi_middle_line_cross_over(adj_prices, period)

        self.assertNotEqual(len(buy_signals), 0)

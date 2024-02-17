import random
from strategies.macd_cross_over import macd_cross_over
from unittest import TestCase


class Test(TestCase):
    def test_macd_cross_over(self):
        adj_prices = random.sample(range(1200, 3400), 400)
        fast_period = 12
        slow_period = 26
        signal_period = 9
        buy_signals, sell_signals = macd_cross_over(adj_prices, fast_period, slow_period, signal_period)

        self.assertNotEqual(len(buy_signals), 0)

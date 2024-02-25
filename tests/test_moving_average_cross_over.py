import random
from strategies.moving_average_cross_over import double_ma_cross_over, double_ma_price_cross_over
from unittest import TestCase


class Test(TestCase):
    def test_double_ma_cross_over(self):
        adj_prices = random.sample(range(1200, 3400), 400)
        fast_period = 20
        slow_period = 50
        buy_signals, sell_signals = double_ma_cross_over(adj_prices, fast_period, slow_period)

        self.assertNotEqual(len(buy_signals), 0)

    def test_double_ma_price_cross_over(self):
        adj_prices = random.sample(range(1200, 3400), 400)
        fast_period = 20
        slow_period = 50
        buy_signals, sell_signals = double_ma_price_cross_over(adj_prices, fast_period, slow_period)

        self.assertNotEqual(len(buy_signals), 0)

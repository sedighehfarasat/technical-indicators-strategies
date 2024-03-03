import random
from strategies.macd_cross_over import macd_cross_over
from strategies.mac import double_ma_cross_over, double_ma_price_cross_over
from strategies.rsi_cross_over import rsi_middle_line_cross_over
from unittest import TestCase


class StrategyTest(TestCase):
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

    def test_macd_cross_over(self):
        adj_prices = random.sample(range(1200, 3400), 400)
        fast_period = 12
        slow_period = 26
        signal_period = 9
        buy_signals, sell_signals = macd_cross_over(adj_prices, fast_period, slow_period, signal_period)

        self.assertNotEqual(len(buy_signals), 0)

    def test_rsi_middle_line_cross_over(self):
        adj_prices = random.sample(range(1200, 3400), 400)
        period = 13
        buy_signals, sell_signals = rsi_middle_line_cross_over(adj_prices, period)

        self.assertNotEqual(len(buy_signals), 0)

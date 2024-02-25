import numpy as np
import random
from performance_and_risk_management.performance_measurement import annualized_sharpe, annualized_sortino
from performance_and_risk_management.risk_management import var_cov_var
from unittest import TestCase


class PerformanceTest(TestCase):
    def test_annualized_sharpe(self):
        prices = random.sample(range(1200, 3400), 252)
        returns = []
        for i in range(len(prices) - 1):
            returns.append((prices[i + 1] - prices[i]) / prices[i])
        risk_free_rate = 0.25
        excess_returns = [ret - risk_free_rate / 252 for ret in returns]
        sharpe = annualized_sharpe(excess_returns, 252)

        self.assertNotEqual(sharpe, 0)

    def test_annualized_sortino(self):
        prices = random.sample(range(1200, 3400), 252)
        returns = []
        for i in range(len(prices) - 1):
            returns.append((prices[i + 1] - prices[i]) / prices[i])
        risk_free_rate = 0.25
        excess_returns = [ret - risk_free_rate / 252 for ret in returns]
        sortino = annualized_sortino(excess_returns, 252)

        self.assertNotEqual(sortino, 0)

    def test_annualized_calmar(self):
        prices = random.sample(range(1200, 3400), 252)
        returns = []
        for i in range(len(prices) - 1):
            returns.append((prices[i + 1] - prices[i]) / prices[i])
        risk_free_rate = 0.25
        excess_returns = [ret - risk_free_rate / 252 for ret in returns]
        calmar = annualized_sortino(excess_returns, 252)

        self.assertNotEqual(calmar, 0)

    def test_var_cov_var(self):
        prices = random.sample(range(1200, 3400), 252)
        returns = []
        for i in range(len(prices) - 1):
            returns.append((prices[i + 1] - prices[i]) / prices[i])
        principal = 100_000_000
        confidence_level = 0.99
        mu = np.mean(returns)
        sigma = np.std(returns)
        var = var_cov_var(principal, confidence_level, mu, sigma)

        self.assertNotEqual(var, 0)

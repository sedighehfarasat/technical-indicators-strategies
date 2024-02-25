"""
Returns:
    Total Return:
    Compound Annual Growth Rate (CAGR):
Risk:
    Annualized Standard Deviation
Maximum Drawdown
Risk/Return Ratio: Risk adjusted return
    Sharpe ratio
    Sortino ratio
    CALMAR ratio
Trade Analysis:
    Total PnL
    Winning count
    Losing count
"""

import numpy as np


def annualized_sharpe(excess_returns, n=252):
    """
    :param excess_returns: assumes that the returns are the excess of those compared to a benchmark.
    :param n: n defaults to 252, which then assumes a stream of daily returns.
    :return: The annualised Sharpe ratio of a returns based on a number of trading periods, n.
    """

    return np.sqrt(n) * np.mean(excess_returns) / np.std(excess_returns)


def annualized_sortino(excess_returns, n=252):
    """
    The Sortino ratio is motivated by the fact that the Sharpe ratio captures both upward and downward volatility .
    However, investors are generally not too bothered when we have significant upward volatility.
    :param excess_returns: assumes that the returns are the excess of those compared to a benchmark.
    :param n: n defaults to 252, which then assumes a stream of daily returns.
    :return: The annualised Sortino ratio of a returns based on a number of trading periods, n.
    """

    downward_excess_returns = list(filter(lambda r: r < 0, excess_returns))

    return np.sqrt(n) * np.mean(excess_returns) / np.std(downward_excess_returns)


def annualized_calmar(excess_returns, n=252):
    """
    One could also argue that investors/traders are concerned solely with the maximum extent of the drawdown,
    rather than the average drawdown.
    :param excess_returns: assumes that the returns are the excess of those compared to a benchmark.
    :param n: n defaults to 252, which then assumes a stream of daily returns.
    :return: The annualised CALMAR ratio of a returns based on a number of trading periods, n.
    """

    return np.sqrt(n) * np.mean(excess_returns) / np.max(excess_returns)

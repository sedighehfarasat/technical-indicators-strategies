"""
VaR provides an estimate, under a given degree of confidence, of the size of a loss from a portfolio
over a given time period.
The "standard" calculation of VaR makes the following assumptions:
- Standard Market Conditions - VaR is not supposed to consider extreme events or "tail
risk", rather it is supposed to provide the expectation of a loss under normal "day-to-day"
operation.
- Volatility and Correlations - VaR requires the volatility of the assets under consideration,
as well as their respective correlations. These two quantities are tricky to estimate
and are subject to continual change.
- Normality of Returns - VaR, in its standard form, assumes the returns of the asset or
portfolio are normally distributed. This leads to more straightforward analytical calculation,
but it is quite unrealistic for most assets.
"""

from scipy.stats import norm


def var_cov_var(p, c, mu, sigma):
    """
    Variance-Covariance calculation of daily Value-at-Risk using confidence level c, with mean of returns mu
    and standard deviation of returns sigma, on a portfolio of value P.
    """

    alpha = norm.ppf(1 - c, mu, sigma)

    return p - p * (alpha + 1)

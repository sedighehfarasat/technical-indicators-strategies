import technical_indicators


def ma_price_cross_over(adj_prices, sma_period):
    # Calculates simple moving average
    sma = technical_indicators.simple_moving_average(adj_prices, sma_period)
    # Generates buy/sell signals
    buy_signals = []
    sell_signals = []
    for i in range(len(sma)):
        if adj_prices[sma_period + i - 1] >= sma[i] and adj_prices[sma_period + i - 1 - 1] < sma[i - 1]:
            buy_signals.append(sma_period + i)
        elif adj_prices[sma_period + i - 1] < sma[i] and adj_prices[sma_period + i - 1 - 1] >= sma[i - 1]:
            sell_signals.append(sma_period + i)

    return buy_signals, sell_signals


def double_ma_cross_over(adj_prices, fast_period, slow_period):
    # Calculates simple moving averages
    fast_sma = list(technical_indicators.simple_moving_average(adj_prices, fast_period))
    slow_sma = list(technical_indicators.simple_moving_average(adj_prices, slow_period))
    del fast_sma[0: slow_period - fast_period]
    # Generates buy/sell signals
    buy_signals = []
    sell_signals = []
    for i in range(len(slow_sma)):
        if fast_sma[i] >= slow_sma[i] and fast_sma[i - 1] < slow_sma[i - 1]:
            buy_signals.append(slow_period + i)
        elif fast_sma[i] < slow_sma[i] and fast_sma[i - 1] >= slow_sma[i - 1]:
            sell_signals.append(slow_period + i)

    return buy_signals, sell_signals

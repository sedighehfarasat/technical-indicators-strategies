import technical_indicators


def ma_price_cross_over(adj_prices, sma_period):
    # Calculates simple moving average
    sma = technical_indicators.simple_moving_average(adj_prices, sma_period)
    # Generates buy/sell signals
    buy_signals = []
    sell_signals = []
    for i in range(len(sma)):
        if adj_prices[sma_period + i - 1] >= sma[i] and adj_prices[sma_period + i - 1 - 1] < sma[i - 1]:
            buy_signals.append(i)
        elif adj_prices[sma_period + i - 1] < sma[i] and adj_prices[sma_period + i - 1 - 1] >= sma[i - 1]:
            sell_signals.append(i)

    return buy_signals, sell_signals


def double_ma_cross_over():
    pass

import technical_indicators


def macd_cross_over(adj_prices, fast_period, slow_period, signal_period):
    # Calculates MACD
    macd = list(technical_indicators.macd(adj_prices, fast_period, slow_period))
    signal = list(technical_indicators.simple_moving_average(macd, signal_period))
    if len(macd) >= len(signal):
        del macd[0: len(macd) - len(signal)]
    else:
        del signal[0: len(signal) - len(macd)]

    # Generates buy/sell signals
    buy_signals = []
    sell_signals = []
    for i in range(len(macd)):
        if macd[i] >= signal[i] and macd[i - 1] < signal[i - 1]:
            buy_signals.append(slow_period + signal_period + i)
        elif macd[i] <= signal[i] and macd[i - 1] > signal[i - 1]:
            sell_signals.append(slow_period + signal_period + i)

    return buy_signals, sell_signals

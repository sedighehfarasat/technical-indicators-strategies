import technical_indicators


def rsi_middle_line_cross_over(adj_prices, period):
    # Calculates RSI
    rsi = list(technical_indicators.rsi(adj_prices, period))
    # Generates buy/sell signals
    buy_signals = []
    sell_signals = []
    for i in range(len(rsi)):
        if rsi[i] >= 50 > rsi[i - 1]:
            buy_signals.append(period + i)
        elif rsi[i] < 50 <= rsi[i - 1]:
            sell_signals.append(period + i)

    return buy_signals, sell_signals

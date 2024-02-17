import market_data
import sys
from strategies.moving_average_cross_over import ma_price_cross_over, double_ma_cross_over


if __name__ == '__main__':
    ins_code = "17914401175772326"
    day = 750
    # sma_period = 20
    fast_period = 20
    slow_period = 50

    # Gets data
    prices = market_data.get_closing_prices(ins_code, day)
    adj_prices = market_data.adjust_closing_prices(prices)

    # Strategy
    # buy_signals, sell_signals = ma_price_cross_over(adj_prices, sma_period)
    buy_signals, sell_signals = double_ma_cross_over(adj_prices, fast_period, slow_period)

    # Backtest the strategy
    if not buy_signals or not sell_signals:
        print('No Signal!')
        sys.exit()

    if sell_signals[0] < buy_signals[0]:
        sell_signals.pop(0)
    if len(buy_signals) > len(sell_signals):
        buy_signals.pop()

    PnL = []
    for i, signal in enumerate(buy_signals):
        PnL.append(adj_prices[sell_signals[i] - 1] - adj_prices[signal - 1])
    profit_count = len(list(filter(lambda n: n >= 0, PnL)))
    loss_count = len(list(filter(lambda n: n < 0, PnL)))
    total_profit = sum(list(filter(lambda n: n >= 0, PnL)))
    total_loss = sum(list(filter(lambda n: n < 0, PnL)))
    total_PnL = total_profit + total_loss

    print('Number of profitable trades: ', profit_count)
    print('Number of losing trades: ', loss_count)
    print(f'Total value of profitable trades: {round(total_profit):,} Rials')
    print(f'Total value of losing trades: {round(total_loss):,} Rials')
    print(f'Total PnL: {round(total_PnL):,} Rials')

import market_data
from strategies.moving_average_cross_over import ma_price_cross_over


if __name__ == '__main__':
    ins_code = "25244329144808274"
    day = 200
    sma_period = 20

    # Gets data
    prices = market_data.get_closing_prices(ins_code, day)
    adj_prices = market_data.adjust_closing_prices(prices)

    # Strategy
    buy_signals, sell_signals = ma_price_cross_over(adj_prices, sma_period)

    # Backtest the strategy
    if sell_signals[0] < buy_signals[0]:
        sell_signals.pop(0)
    if len(buy_signals) > len(sell_signals):
        buy_signals.pop()

    PnL = []
    for i, signal in enumerate(buy_signals):
        PnL.append(adj_prices[sma_period + sell_signals[i] - 1] - adj_prices[sma_period + signal - 1])
    profit_count = len(list(filter(lambda n: n >= 0, PnL)))
    loss_count = len(list(filter(lambda n: n < 0, PnL)))
    total_profit = sum(list(filter(lambda n: n >= 0, PnL)))
    total_loss = sum(list(filter(lambda n: n < 0, PnL)))
    total_PnL = total_profit + total_loss

    print('Number of profitable trades: ', profit_count)
    print('Number of losing trades: ', loss_count)
    print('Total value of profitable trades (in Rials): ', round(total_profit))
    print('Total value of losing trades (in Rials): ', round(total_loss))
    print('Total PnL (in Rials): ', round(total_PnL))

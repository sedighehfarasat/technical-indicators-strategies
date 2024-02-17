import market_data
import sys
from strategies.moving_average_cross_over import ma_price_cross_over, double_ma_cross_over
from strategies.rsi_cross_over import rsi_middle_line_cross_over


if __name__ == '__main__':
    buy_signals, sell_signals = [], []
    PnL = []

    # Gets data
    ins_code = input("Please enter INS code: ")
    day = int(input("How many days of data do you need? "))
    prices = market_data.get_closing_prices(ins_code, day)
    adj_prices = market_data.adjust_closing_prices(prices)

    # Strategies
    print("Select strategy: ")
    print("1. Moving Average Cross Over")
    print("2. Double Moving Averages Cross Over")
    print("3. RSI Cross Over")
    strategy = int(input())
    if strategy == 1:
        sma_period = int(input("Please enter the moving average period: "))
        buy_signals, sell_signals = ma_price_cross_over(adj_prices, sma_period)
    elif strategy == 2:
        fast_period, slow_period = map(int, input("Please enter fast and slow moving average period: ").split(' '))
        buy_signals, sell_signals = double_ma_cross_over(adj_prices, fast_period, slow_period)
    elif strategy == 3:
        rsi_period = int(input("Please enter the RSI period: "))
        buy_signals, sell_signals = rsi_middle_line_cross_over(adj_prices, rsi_period)
    else:
        print("Please enter the correct number of strategy.")

    # Backtest the strategy
    if not buy_signals or not sell_signals:
        print('No Signal!')
        sys.exit()

    if sell_signals[0] < buy_signals[0]:
        sell_signals.pop(0)
    if len(buy_signals) > len(sell_signals):
        buy_signals.pop()

    for i, signal in enumerate(buy_signals):
        PnL.append(adj_prices[sell_signals[i] - 1] - adj_prices[signal - 1])
    profit_count = len(list(filter(lambda n: n >= 0, PnL)))
    loss_count = len(list(filter(lambda n: n < 0, PnL)))
    total_profit = sum(list(filter(lambda n: n >= 0, PnL)))
    total_loss = sum(list(filter(lambda n: n < 0, PnL)))
    total_PnL = total_profit + total_loss

    print('-----------------------------------------------')
    print('Number of profitable trades: ', profit_count)
    print('Number of losing trades: ', loss_count)
    print(f'Total value of profitable trades: {round(total_profit):,} Rials')
    print(f'Total value of losing trades: {round(total_loss):,} Rials')
    print(f'Total PnL: {round(total_PnL):,} Rials')
    print('-----------------------------------------------')


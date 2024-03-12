import datetime

import pandas as pd
from matplotlib import pyplot as plt
from trading_engine.backtest import Backtest
from trading_engine.data import TsetmcHistoricCSVDataHandler
from trading_engine.execution import SimulatedExecutionHandler
from trading_engine.portfolio import Portfolio
from strategies.moving_average_cross_over import MovingAverageCrossStrategy


if __name__ == "__main__":

    symbols = ['Pars.Ceram', 'Razak.Lab.']
    for s in symbols:
        print('--------------------------')
        print(s)
        print('--------------------------')
        csv_dir = '~/Downloads'
        symbol_list = [s]
        initial_capital = 100_000_000.0
        heartbeat = 0.0
        start_date = datetime.datetime(2023, 6, 22)
        backtest = Backtest(
            csv_dir, symbol_list, initial_capital, heartbeat,
            start_date, TsetmcHistoricCSVDataHandler, SimulatedExecutionHandler,
            Portfolio, MovingAverageCrossStrategy
        )
        backtest.simulate_trading()

    # # Plot performance
    # data = pd.read_csv(
    #     "equity.csv",
    #     header=0,
    #     parse_dates=True,
    #     index_col=0
    # ).sort_index()
    #
    # fig = plt.figure()
    # fig.patch.set_facecolor('white')
    #
    # # Plot the equity curve
    # ax1 = fig.add_subplot(311, ylabel='Portfolio Returns, % ')
    # data['equity_curve'].plot(ax=ax1, color="blue", lw=2.)
    # plt.grid(True)
    #
    # # Plot the returns
    # ax2 = fig.add_subplot(312, ylabel='Daily Portfolio Returns, % ')
    # data['returns'].plot(ax=ax2, color="black", lw=2.)
    # plt.grid(True)
    #
    # # Plot the drawdown
    # ax3 = fig.add_subplot(313, ylabel='Drawdowns, % ')
    # data['drawdown'].plot(ax=ax3, color="red", lw=2.)
    # plt.grid(True)
    #
    # plt.show()

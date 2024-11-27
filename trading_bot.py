from datetime import datetime
from lumibot.backtesting import YahooDataBacktesting
from lumibot.credentials import broker
from lumibot.credentials import IS_BACKTESTING
from lumibot.strategies import Strategy
from lumibot.traders import Trader

class BuyEveryDay(Strategy):
  def initialize(self, symbol=""):
    self.sleeptime = "10D"

  def on_trading_iteration(self):
    symbol = "AAPL"
    price = self.get_last_price(symbol)
    quantity = 10 / price
    order = self.create_order(symbol, quantity, "buy")
    self.submit_order(order)

if __name__ == "__main__":
  if IS_BACKTESTING:
    start = datetime(2015,1,1)
    end = datetime(2023,12,31)
    BuyEveryDay.backtest(
      YahooDataBacktesting,
      start,
      end
    )
  else:
    strategy = BuyEveryDay(broker=broker)
    trader = Trader()
    trader.add_strategy(strategy)
    trader.run_all()
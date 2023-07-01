from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.stream import TradingStream
from alpaca_trade_api.rest import REST
import config
import pandas as pd


#displaying user account stuff here
client=TradingClient(config.API_KEY, config.SECRET_KEY, paper=True)
account= dict((client.get_account()))
for k, v in account.items():
    print(f"{k:30}{v}")




# #intiating order market request
# order_details = MarketOrderRequest(
#     symbol ="SPY",
#     qty=10,
#     side = OrderSide.BUY,
#     time_in_force = TimeInForce.DAY
    
# )

client = REST(config.API_KEY, config.SECRET_KEY)
# Get the last trade for a stock
symbol = "AAPL"
trade = client.last_trade(symbol)

# Calculate the expected price
expected_price = trade.price

# Display the expected price
print(f"Expected price for {symbol}: {expected_price:.2f}")




assets = [asset for asset in client.get_all_positions()]
#object for each asset
positions = [(asset.symbol, asset.qty, asset.current_price) for asset in assets]
print("Postions")
#printing out a table
print(f"{'Symbol':9}{'Qty':>4}{'Value':>15}")
print("-" * 28)
#loop through any assest i have 
for position in positions:
    print(f"{position[0]:9}{position[1]:>4}{float(position[1]) * float(position[2]):>15.2f}")

client.close_all_positions(cancel_orders=True)
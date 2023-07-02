from alpaca.trading.client import TradingClient
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.stream import TradingStream
from alpaca_trade_api.rest import REST
import config
import pandas as pd


def display_account_info():
    """
    Display information about the account using the Alpaca API.
    """
    account = client.get_account()
    for k, v in account._raw.items():
        print(f"{k:30}{v}")


client = REST(config.API_KEY, config.SECRET_KEY, api_version='v2')

def get_expected_price(symbol: str) -> float:
    """
    Calculate the expected price of a stock using the Alpaca API.

    :param symbol: The symbol of the stock to retrieve the expected price for.
    :return: The expected price of the stock.
    """
    trade = client.last_trade(symbol)
    expected_price = trade.price
    return expected_price

def display_positions():
    """
    Display the positions in the account using the Alpaca API.
    """
    assets = client.list_positions()
    positions = [(asset.symbol, asset.qty, asset.current_price) for asset in assets]
    print("Positions")
    print(f"{'Symbol':9}{'Qty':>4}{'Value':>15}")
    print("-" * 28)
    for position in positions:
        print(f"{position[0]:9}{position[1]:>4}{float(position[1]) * float(position[2]):>15.2f}")


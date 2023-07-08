from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

# Returns a daily DataFrame
def get_stock_data(stock_name, start_date, end_date):
    
    ## INCOMPLETE 
    ## if start_date == "start":
    
    if end_date == "today":
        end_date = datetime.now()
    
    client=CryptoHistoricalDataClient()

    request=CryptoBarsRequest(
        symbol_or_symbols = [stock_name],
        timeframe = TimeFrame.Day,
        start = datetime.strptime(start_date, '%Y-%m-%d'),
        end = datetime.strptime(end_date,'%Y-%m-%d') 
    )
    data=client.get_crypto_bars(request, feed="us")
    return data

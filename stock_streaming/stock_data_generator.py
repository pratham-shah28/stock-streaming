import json
import os
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest, StockLatestTradeRequest
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')

client = StockHistoricalDataClient(api_key, secret_key)

# multi symbol request - single symbol is similar
multisymbol_request_params = StockLatestTradeRequest(symbol_or_symbols=["SPY", "GLD", "TLT"])

latest_multisymbol_quotes = client.get_stock_latest_trade(multisymbol_request_params)

gld_latest_ask_price = latest_multisymbol_quotes["TLT"].price

print(gld_latest_ask_price)
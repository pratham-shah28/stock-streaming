import requests
import json
import os
from alpaca.data.live.stock import StockDataStream
from alpaca.data.requests import StockLatestQuoteRequest
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')
stream_data_wss = None
data_client = StockLatestQuoteRequest(symbol_or_symbols='AAPL', feed='iex')
print(data_client.dict)

stock_data_stream_client = StockDataStream(api_key, secret_key, url_override = stream_data_wss)

async def stock_data_stream_handler(data):
    print(data)

symbols = ['AAPL']

stock_data_stream_client.subscribe_quotes(stock_data_stream_handler, *symbols)
stock_data_stream_client.run()


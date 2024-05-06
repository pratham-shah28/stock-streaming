import json
import os
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestTradeRequest
from dotenv import load_dotenv
from confluent_kafka import Producer

load_dotenv()

api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')


class StockDataGenerator():
    def __init__(self, api_key, secret_key, stock_symbol, producer, partition_idx, topic_name):
        self.api_key = api_key
        self.secret_key = secret_key
        self.stock_symbol = stock_symbol
        self.client = StockHistoricalDataClient(api_key, secret_key)
        self.producer = producer
        self.partition_idx = partition_idx
        self.topic_name = topic_name

    def get_ltp(self):
        multiSymbol_request_params = StockLatestTradeRequest(symbol_or_symbols=[self.stock_symbol])
        latest_multiSymbol_quotes = self.client.get_stock_latest_trade(multiSymbol_request_params)
        ltp = latest_multiSymbol_quotes[self.stock_symbol].price
        ltp_bytes = str(ltp).encode('utf-8')
        self.producer.produce(self.topic_name, key=self.stock_symbol, value=ltp_bytes, partition=self.partition_idx,)
        self.producer.flush()


# sgd = StockDataGenerator(api_key,
#                          secret_key,
#                          'AAPL',
#                          Producer,
#                          1,
#                          'stock')
# sgd.get_ltp()
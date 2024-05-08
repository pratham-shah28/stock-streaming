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
        self.multiSymbol_request_params = StockLatestTradeRequest(symbol_or_symbols=[self.stock_symbol])

    def get_ltp(self):
        latest_multiSymbol_quotes = self.client.get_stock_latest_trade(self.multiSymbol_request_params)
        ltp = latest_multiSymbol_quotes[self.stock_symbol].price
        timestamp = latest_multiSymbol_quotes[self.stock_symbol].timestamp
        timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        data = {
            "timestamp": timestamp_str,
            "ltp": ltp
        }
        # Convert the dictionary to JSON string
        data_json = json.dumps(data)
        # Encode the JSON string to bytes
        data_bytes = data_json.encode('utf-8')

        self.producer.produce(topic=self.topic_name, key=self.stock_symbol, value=data_bytes, partition=self.partition_idx,)
        self.producer.flush()



# sgd = StockDataGenerator(api_key,
#                          secret_key,
#                          'AAPL',
#                          Producer,
#                          1,
#                          'stock')
# sgd.get_ltp()
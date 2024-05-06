from stock_streaming.stock_generation.generate_price_producer import StockGenerator
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")
kafka_server = 'localhost:9092'
topic = 'myFirstTopic'
# sdg = StockGenerator('AAPL',api_key,
#                          secret_key,
#                          'AAPL',
#                          Producer,
#                          1,
#                          'stock')

sdg = StockGenerator('AAPL',
                     kafka_server,
                     topic,
                     api_key,
                     secret_key,
                     '05-06/2024',
                     1)
print(sdg.realtime_price_generation())
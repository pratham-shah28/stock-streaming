from generate_price_producer import StockGenerator
import os
from dotenv import load_dotenv
import time


load_dotenv()
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")
kafka_server = 'host.docker.internal:9092'
topic = 'myFirstTopic'


sdg = StockGenerator('AAPL',
                     kafka_server,
                     topic,
                     api_key,
                     secret_key,
                     '05-06/2024',
                     0)

while True:
    sdg.realtime_price_generation()
    time.sleep(1)
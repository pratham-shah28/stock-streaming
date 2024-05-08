from confluent_kafka import Consumer, KafkaError, TopicPartition

def consume_stock_data(topic_name):
    conf = {
        'bootstrap.servers': 'localhost:9092',  # Kafka broker address
        'group.id': 'my_consumer_group',  # Consumer group ID
        'auto.offset.reset': 'earliest'  # Start consuming from the earliest available message
    }
    topic_name = 'myFirstTopic'
    partition_id = 0  # The partition ID to which you want to assign the consumer
    topic_partition = TopicPartition(topic_name, partition_id)


    consumer = Consumer(conf)
    # consumer.subscribe(['myFirstTopic'])
    consumer.assign([topic_partition])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)  # Poll for new messages
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            # Process the message
            print('Received message: {}'.format(msg.value().decode('utf-8')))
    finally:
        consumer.close()

if __name__ == '__main__':
    topic_name = 'stock'  # Change this to your topic name
    consume_stock_data(topic_name)
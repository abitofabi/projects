from confluent_kafka import Consumer,KafkaException,KafkaError
import sys

# Kafka Config

conf = {
    'bootstrap.servers': 'pkc-921jm.us-east-2.aws.confluent.cloud:9092', #located in cluster settings in conf cloud
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms':'PLAIN',
    'sasl.username':'7OTGJZCRH43JBUYT',
    'sasl.password':'cfltv7QRInPaxwKgzt7K1x4hABRTA7crphPYdNGMD1yG0opo0qHUXUO+eIPwCnRg',
    'group.id':'my-consumer-group',
    'auto.offset.reset':'earliest'
}

#create producer instance

consumer = Consumer(conf)
topic = 'ride_events'
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f'End of partition reached {msg.topic()} [{msg.partition()}]')
            else:
                print(f'Error: {msg.error()}')
        else:
            print(f'Received message: {msg.value().decode("utf-8")}')
except KeyboardInterrupt:
    print("Aborted by user")
finally:
    consumer.close()
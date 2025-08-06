from confluent_kafka import Producer
import time
import json
import random

# Kafka Config

conf = {
    'bootstrap.servers': 'pkc-921jm.us-east-2.aws.confluent.cloud:9092', #located in cluster settings in conf cloud
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms':'PLAIN',
    'sasl.username':'7OTGJZCRH43JBUYT',
    'sasl.password':'cfltv7QRInPaxwKgzt7K1x4hABRTA7crphPYdNGMD1yG0opo0qHUXUO+eIPwCnRg'
}

#create producer instance

producer = Producer(conf)

def delivery_report(err,msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else :
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def generate_ride_requests():
    return {
        "user_id": random.randint(1000, 9999),
        "location": random.choice(["Toronto", "Vancouver", "Montreal", "Calgary"]),
        "timestamp": int(time.time()),
        "ride_type": random.choice(["standard", "premium", "pool"])
    }
for _ in range(10):
    data = generate_ride_requests()
    producer.produce(
        topic="ride_events_v2",
        value=json.dumps(data),
        callback=delivery_report
    )
    producer.poll(0)
    time.sleep(1)

producer.flush()

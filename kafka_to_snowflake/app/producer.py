from confluent_kafka import Producer
import os
import json
from dotenv import load_dotenv
from utils.generator import generate_ride_requests

load_dotenv()

# Kafka Config

conf = {
    'bootstrap.servers':os.getenv("BOOTSTRAP_SERVERS"), #located in cluster settings in conf cloud
    'security.protocol':'SASL_SSL',
    'sasl.mechanisms':'PLAIN',
    'sasl.username':os.getenv("API_KEY"),#,
    'sasl.password':os.getenv("API_SECRET")#'
}

#create producer instance

producer = Producer(conf)

def delivery_report(err,msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else :
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def produce_ride_event():
    message = generate_ride_requests()
    producer.produce("ride_events_v2",
                     key=str(message["user_id"]),
                     value=json.dumps(message).encode("utf-8"),
                     callback=delivery_report)
    producer.flush()


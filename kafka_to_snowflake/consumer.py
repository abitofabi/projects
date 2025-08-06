from confluent_kafka import Consumer,KafkaException,KafkaError
import sys

# Kafka Config

conf = KafkaConsumer(
    'bootstrap.servers': 'pkc-921jm.us-east-2.aws.confluent.cloud:9092', #located in cluster settings in conf cloud
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms':'PLAIN',
   # 'sasl.username':'7OTGJZCRH43JBUYT',
    #'sasl.password':'cfltv7QRInPaxwKgzt7K1x4hABRTA7crphPYdNGMD1yG0opo0qHUXUO+eIPwCnRg',
    #'group.id':'my-consumer-group',
    'auto.offset.reset':'earliest'
)
#snowflake config

conn = snowflake.connector.connect(
    user='kafka_snow_app_user',
    password='K1afka_snow_app_user',
    account='<YOUR_ACCOUNT>.snowflakecomputing.com',
    warehouse='RIDE_SHARE',
    database='RIDE_SHARE_DB',
    schema='PUBLIC',
    role='KAFKA_SNOW_ROLE'
)
#create producer instance
cursor = conn.cursor()

# Process messages
for message in consumer:
    data = message.value
    print(f"Received: {data}")

    try:
        cursor.execute("""
            INSERT INTO ride_requests (ride_id, user_id, location, timestamp, ride_type)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data.get('ride_id'),
            data.get('user_id'),
            data.get('location'),
            data.get('timestamp'),
            data.get('ride_type')
        ))
        print("✅ Inserted into Snowflake.")
    except Exception as e:
        print("❌ Error inserting into Snowflake:", e)

# Clean up (optional if you run this as a daemon)
cursor.close()
conn.close()
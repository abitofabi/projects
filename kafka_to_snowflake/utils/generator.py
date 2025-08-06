# utils/generator.py
import random
import time

def generate_ride_requests():
    return {
        "user_id": random.randint(1000, 9999),
        "location": random.choice(["Toronto", "Vancouver", "Montreal", "Calgary"]),
        "timestamp": int(time.time()),
        "ride_type": random.choice(["standard", "premium", "pool"])
    }
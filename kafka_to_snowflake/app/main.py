from fastapi import FastAPI
from app.producer import produce_ride_event
#init FASTAPI
app=FastAPI()

@app.get("/")
def root():
    return{"message":"Kafka service is running"}

@app.post("/produce")
def produce():
    produce_ride_event()
    return{"status":"Event sent"}
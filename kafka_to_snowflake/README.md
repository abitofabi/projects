# Ride Demand Stream Microservice with Kafka and Snowflake

## Overview

This project demonstrates a real-time data pipeline for a ride-sharing company scenario (think Uber or Lyft). It simulates how ride booking events are produced, consumed, and ingested into a cloud data warehouse for analytics.

---

## What it does

- **Produces** JSON ride request events to a Kafka topic (`ride_events`) using a Python microservice.
- **Consumes** these events from Kafka and streams them into a Snowflake table for analytics.
- Utilizes **Confluent Cloud Kafka** for managed Kafka infrastructure.
- Uses **Snowflake Kafka Sink Connector** to automatically ingest Kafka messages into Snowflake.
- Provides a simple **FastAPI** microservice with an endpoint to trigger event production.

---

## Why this project?

- To learn and showcase modern data engineering skills with real-time streaming.
- To demonstrate integration between Kafka (messaging) and Snowflake (data warehouse).
- To build a modular, maintainable microservice using Python and FastAPI.
- To practice infrastructure setup on cloud-managed services (Confluent Cloud, Snowflake).

---

## Project Structure
- app/
  - __init__.py
  - main.py
  - producer.py
  - utils/
    - __init__.py
    - generator.py
- consumer.py
- requirements.txt
- README.md
- .env


---

## How to Run

### Prerequisites

- Python 3.8+
- Confluent Cloud account with Kafka cluster & topic created (`ride_events`)
- Snowflake account with database, schema, user, role, and sink connector configured
- Environment variables for API keys, secrets stored in `.env`

### Setup Steps

1. **Clone repo** and create a Python virtual environment:
   ```bash
   git clone <repo_url>
   cd <repo_folder>
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. **Configure `.env`** with your Confluent and Snowflake credentials:
   ```env
   CONFLUENT_API_KEY=...
   CONFLUENT_API_SECRET=...
   SNOWFLAKE_USER=...
   SNOWFLAKE_PRIVATE_KEY=...
   ```

3. **Run the FastAPI microservice**:
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Produce events** by sending a POST request:
   ```bash
   curl -X POST http://localhost:8000/produce
   ```
   This will produce a ride event message to the Kafka topic.

5. **Verify data** is ingested into Snowflake by querying your `ride_requests` table.

---

## Code Highlights

- `generator.py` - Creates randomized ride event JSON data with fields like `user_id`, `location`, `timestamp`, and `ride_type`.
- `producer.py` - Connects to Kafka and publishes ride event messages.
- `main.py` - FastAPI app exposes endpoints to produce events and check service health.
- Snowflake Kafka Sink Connector is configured separately in Confluent Cloud UI to move messages automatically to Snowflake.
- Local `consumer.py` can be used for testing or debugging Kafka consumption.

---

## How this project evolved

- Initially, started with a simple Python Kafka producer and consumer using Confluent Cloud.
- Setup Snowflake as the destination data warehouse and solved schema and permission issues.
- Added Snowflake Kafka Sink Connector to automate data ingestion.
- Modularized code by separating event generation logic.
- Added FastAPI microservice to provide an HTTP interface for producing events.
- Used `.env` for secure environment variable management.
- Documented steps carefully for repeatability and clarity.

---

## What’s next?

- Implement monitoring and alerting for the microservice.
- Add schema validation with Pydantic in FastAPI.
- Build dashboards on Snowflake data for analytics.
- Extend to handle other event types and enrich data.
- Containerize the microservice with Docker for deployment.
- Automate deployment with CI/CD pipelines.

---

## Resources & References

- [Confluent Cloud Docs](https://docs.confluent.io/cloud/current/overview.html)
- [Snowflake Kafka Connector](https://docs.snowflake.com/en/user-guide/kafka-connector.html)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Kafka Python Client](https://docs.confluent.io/platform/current/clients/python.html)

---

*Feel free to reach out if you want help extending this or adding more features!* 🚀

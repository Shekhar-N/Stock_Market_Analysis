📈 Stock Market Near Real-Time Analysis using PySpark
📌 Project Overview

This project implements a near real-time stock market analytics pipeline using PySpark Structured Streaming and open-source tools only.

Due to the lack of free true real-time stock exchange feeds, the system uses near real-time data ingestion and a file-based streaming architecture to simulate a real-world streaming pipeline. This approach is widely accepted for learning and academic projects.

The pipeline continuously ingests stock price data, processes it using Spark streaming, computes technical indicators, stores results in a columnar format, and visualizes trends on an interactive dashboard.

🎯 Objectives

Build a complete end-to-end data pipeline

Learn Structured Streaming concepts in Spark

Perform window-based aggregations

Store analytics data efficiently using Parquet

Visualize near real-time trends using Streamlit

Design a project that is resume and interview ready

🏗️ Architecture
Stock Data Source (Yahoo Finance - Free)
        ↓
Python Ingestion Service
        ↓
File-based Streaming (JSON events)
        ↓
PySpark Structured Streaming
        ↓
Parquet Storage
        ↓
Streamlit Dashboard

Why file-based streaming?

Free and simple to set up

Supported natively by Spark

Mimics Kafka-style micro-batches

Ideal for learning streaming fundamentals

🧰 Tech Stack
Layer	Technology
Language	Python
Streaming Engine	PySpark (Structured Streaming)
Data Source	Yahoo Finance (near real-time)
Storage	Parquet
Visualization	Streamlit
Environment	Local (no cloud, no paid APIs)

📂 Project Structure
stock-market-analysis/
├── ingestion/        # Data collection
├── streaming/        # Spark streaming logic
├── batch/            # Offline analytics
├── analytics/        # Indicator logic
├── visualization/    # Dashboard
├── config/           # App & Spark configs
├── utils/            # Helpers (logging, time)
├── data/             # Raw, processed & checkpoints
└── scripts/          # Run scripts


This structure follows industry-style separation of concerns.

🔄 Data Flow Explained

Ingestion

Python script fetches near real-time stock prices

Each price update is written as a JSON event

Streaming Processing

Spark Structured Streaming reads JSON files

Event time is extracted and parsed

Windowed aggregations (5-minute moving average) are computed

Storage

Aggregated results are written in Parquet format

Enables efficient querying and visualization

Visualization

Streamlit reads processed Parquet files

Interactive line charts show price trends

📊 Analytics Implemented

5-minute windowed moving average of stock prices

Symbol-wise aggregation

Event-time based processing (not processing-time)

▶ How to Run the Project
1️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Linux / WSL
# OR
venv\Scripts\Activate.ps1  # Windows

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start data ingestion
python ingestion/stock_data_collector.py

4️⃣ Start Spark streaming (new terminal)
spark-submit streaming/stock_stream_processor.py

5️⃣ Start visualization dashboard (new terminal)
streamlit run visualization/streamlit_app.py


Open in browser:

http://localhost:8501

⚠ Limitations

Uses near real-time data (not tick-level exchange data)

File-based streaming instead of Kafka

Designed for learning and local execution

These trade-offs were made intentionally to keep the project free, transparent, and educational.

🚀 Future Enhancements

Add more indicators (EMA, RSI, Bollinger Bands)

Integrate Kafka for real message streaming

Add alerting for price spikes

Containerize using Docker

Deploy dashboard to cloud

💬 How to Explain This Project in Interviews

“I built a near real-time stock market analytics pipeline using PySpark Structured Streaming. Since free real-time exchange feeds are restricted, I designed a file-based streaming ingestion system that simulates real streaming behavior. Spark processes the data using event-time windows, stores results in Parquet, and the trends are visualized using Streamlit.”

🧑‍🎓 Author Notes

This project was built independently for learning purposes, focusing on core data engineering concepts rather than paid tools or managed services.
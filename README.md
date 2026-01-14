# 📈 Stock Market Near Real-Time Analysis using PySpark

### 📌 Project Overview
This project implements a **near real-time stock market analytics pipeline** using **PySpark Structured Streaming** and open-source tools only.

Due to the lack of free true real-time stock exchange feeds, the system uses **near real-time data ingestion** and a **file-based streaming architecture** to simulate a real-world streaming pipeline. This approach is widely accepted for learning and academic projects.

### 🚀 Pipeline Functionality
The pipeline is designed to handle the following tasks:
* **Continuous Ingestion:** Monitors and ingests stock price data as it arrives.
* **Spark Processing:** Utilizes Spark Structured Streaming for data transformation.
* **Technical Indicators:** Computes key financial metrics and indicators on the fly.
* **Columnar Storage:** Stores processed results in a columnar format (e.g., Parquet) for efficient querying.
* **Visualization:** Displays trends and analysis on an interactive dashboard.

## 🎯 Objectives

* **Build a complete end-to-end data pipeline:** Develop a seamless flow from data ingestion to visualization.
* **Learn Structured Streaming concepts in Spark:** Master the fundamentals of real-time data processing using PySpark.
* **Perform window-based aggregations:** Implement complex temporal calculations and rolling averages on streaming data.
* **Store analytics data efficiently using Parquet:** Utilize columnar storage formats to optimize disk space and query performance.
* **Visualize near real-time trends using Streamlit:** Create an interactive, Python-based dashboard for data storytelling.
* **Design a project that is resume and interview ready:** Focus on industry-standard tools and architectural patterns.

## 🏗️ Architecture

The pipeline follows a decoupled architecture, moving data from ingestion to visualization through the following stages:

1. **Stock Data Source:** Fetches data via Yahoo Finance (Free API).
2. **Python Ingestion Service:** Scripts to pull and format the raw data.
3. **File-based Streaming:** Raw JSON events act as the landing zone for the stream.
4. **PySpark Structured Streaming:** The core processing engine for transformations.
5. **Parquet Storage:** Efficient, columnar storage for processed analytics.
6. **Streamlit Dashboard:** The presentation layer for interactive visualization.

#### Why file-based streaming?

* **Free and simple to set up:** Eliminates the need for expensive cloud infrastructure or complex messaging brokers like Kafka or Kinesis.
* **Supported natively by Spark:** PySpark includes built-in support for monitoring directories and processing new files as they arrive.
* **Mimics Kafka-style micro-batches:** By dropping files into a folder, you can simulate how a message queue triggers micro-batch processing.
* **Ideal for learning streaming fundamentals:** Allows you to focus on core concepts like windowing and watermarking without the overhead of managing a distributed cluster.

## 🧰 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Language** | Python |
| **Streaming Engine** | PySpark (Structured Streaming) |
| **Data Source** | Yahoo Finance (near real-time) |
| **Storage** | Parquet |
| **Visualization** | Streamlit |
| **Environment** | Local (no cloud, no paid APIs) |

## 📂 Project Structure

```text
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
```

## 🔄 Data Flow Explained

### 1. Ingestion
* **Source:** A Python script fetches near real-time stock prices from the Yahoo Finance API.
* **Format:** Each price update is serialized and written to the landing directory as an individual **JSON event**.

### 2. Streaming Processing
* **Read:** PySpark Structured Streaming monitors the landing directory and reads new JSON files as they arrive.
* **Parse:** The `event_time` is extracted and cast to a timestamp for time-series analysis.
* **Transform:** Windowed aggregations (e.g., **5-minute moving averages**) are computed over the stream to smooth out price volatility.

### 3. Storage
* **Sink:** Aggregated results are written to disk in **Parquet format**.
* **Optimization:** Using Parquet enables efficient columnar querying, which significantly speeds up the visualization layer.

### 4. Visualization
* **Dashboard:** Streamlit monitors the processed Parquet files.
* **Output:** Interactive line charts are rendered to show near real-time price trends and technical indicators.


## 📊 Analytics Implemented

The core logic of this pipeline focuses on time-series analysis and stateful streaming:

* **5-minute windowed moving average:** Calculates the average stock price over a rolling 5-minute interval to smooth out noise and identify short-term trends.
* **Symbol-wise aggregation:** Groups incoming data by the stock ticker (symbol), allowing the pipeline to handle multiple stocks simultaneously.
* **Event-time based processing:** Processes data based on when the trade actually occurred (*Event Time*), rather than when the data reached the Spark cluster (*Processing Time*).
    * Ensures accuracy in the case of delayed data or out-of-order events.
 
## ▶ How to Run the Project

Follow these steps in order to initialize the environment and start the pipeline.

### 1️⃣ Create and Activate Virtual Environment

```bash
# Create the environment
python -m venv venv

# Activate (Linux / WSL)
source venv/bin/activate

# Activate (Windows)
.\venv\Scripts\Activate.ps1
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start data ingestion

```bash
python ingestion/stock_data_collector.py
```

### 4️⃣ Start Spark streaming (new terminal)

```bash
spark-submit streaming/stock_stream_processor.py
```

### 5️⃣ Start visualization dashboard (new terminal)

```bash
streamlit run visualization/streamlit_app.py
```

Open in browser:

```arduino
http://localhost:8501
```

## ⚠ Limitations

* Uses near real-time data (not tick-level exchange data)
* File-based streaming instead of Kafka
* Designed for learning and local execution

These trade-offs were made intentionally to keep the project free, transparent, and educational.

## 🚀 Future Enhancements

* Add more indicators (EMA, RSI, Bollinger Bands)

* Integrate Kafka for real message streaming

* Add alerting for price spikes

* Containerize using Docker

* Deploy dashboard to cloud

## 🧑‍🎓 Author Notes

This project was built **independently for learning purposes**, focusing on core data engineering concepts rather than paid tools or managed services.

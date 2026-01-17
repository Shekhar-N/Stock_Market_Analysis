import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.graph_objects as go

st.set_page_config(page_title="Stock Market Dashboard", layout="wide")

st.title("📈 Near Real-Time Stock Market Dashboard")

DATA_PATH = Path("data/processed/indicators")

# --------------------------------
# Load parquet data
# --------------------------------
if not DATA_PATH.exists():
    st.warning("No processed data yet. Start ingestion.")
    st.stop()

files = list(DATA_PATH.rglob("*.parquet"))

if not files:
    st.warning("Waiting for streaming data...")
    st.stop()

df = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)

# --------------------------------
# Extract window timestamps
# --------------------------------
df["start_time"] = df["window"].apply(lambda x: x["start"])
df["end_time"] = df["window"].apply(lambda x: x["end"])

# --------------------------------
# Stock selector
# --------------------------------
symbol = st.selectbox("Select Stock", sorted(df["symbol"].unique()))
filtered = df[df["symbol"] == symbol].sort_values("start_time")

# --------------------------------
# Build synthetic OHLC
# --------------------------------
ohlc = pd.DataFrame(
    {
        "Time": filtered["start_time"],
        "Open": filtered["avg_price"],
        "High": filtered["avg_price"],
        "Low": filtered["avg_price"],
        "Close": filtered["avg_price"],
    }
)

# --------------------------------
# Candlestick chart
# --------------------------------
fig = go.Figure(
    data=[
        go.Candlestick(
            x=ohlc["Time"],
            open=ohlc["Open"],
            high=ohlc["High"],
            low=ohlc["Low"],
            close=ohlc["Close"],
        )
    ]
)

fig.update_layout(
    title=f"{symbol} Candlestick Chart (Window Avg Price)",
    xaxis_title="Time",
    yaxis_title="Price",
    xaxis_rangeslider_visible=False,
    height=600,
)

st.plotly_chart(fig, use_container_width=True)

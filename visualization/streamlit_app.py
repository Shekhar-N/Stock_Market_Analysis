import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Stock Market Dashboard", layout="wide")

st.title("📈 Near Real-Time Stock Market Dashboard")

DATA_PATH = Path("data/processed/indicators")

if not DATA_PATH.exists():
    st.warning("No processed data yet. Start Spark streaming.")
    st.stop()

files = list(DATA_PATH.rglob("*.parquet"))

if not files:
    st.warning("Waiting for streaming data...")
    st.stop()

df = pd.concat([pd.read_parquet(f) for f in files])

df["start_time"] = df["window"].apply(lambda x: x["start"])
df["end_time"] = df["window"].apply(lambda x: x["end"])

symbol = st.selectbox("Select Stock", df["symbol"].unique())

filtered = df[df["symbol"] == symbol]

st.line_chart(filtered.set_index("start_time")["avg_price"])

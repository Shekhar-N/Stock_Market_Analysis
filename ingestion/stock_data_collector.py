import time
import json
from datetime import datetime, timezone
import yfinance as yf
from pathlib import Path

# -------------------------------
# Configuration
# -------------------------------
SYMBOLS = ["AAPL", "MSFT", "GOOGL"]  # change as needed
REFRESH_INTERVAL = 60  # seconds
OUTPUT_DIR = Path("data/raw/stock_stream")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# -------------------------------
# Helper function
# -------------------------------
def fetch_stock_price(symbol: str) -> dict:
    ticker = yf.Ticker(symbol)
    data = ticker.fast_info

    return {
        "symbol": symbol,
        "price": data.get("last_price"),
        "open": data.get("open"),
        "high": data.get("day_high"),
        "low": data.get("day_low"),
        "volume": data.get("last_volume"),
        "currency": data.get("currency"),
        "event_time": datetime.now(timezone.utc).isoformat(),
    }


# -------------------------------
# Main loop
# -------------------------------
def stream_stock_data():
    print("Starting stock data ingestion...")
    print(f"Symbols: {SYMBOLS}")
    print(f"Refresh interval: {REFRESH_INTERVAL} seconds")

    while True:
        try:
            for symbol in SYMBOLS:
                record = fetch_stock_price(symbol)

                # Write one JSON file per batch
                filename = OUTPUT_DIR / f"{symbol}_{int(time.time())}.json"

                with open(filename, "w") as f:
                    json.dump(record, f)

                print(f"[{record['event_time']}] {symbol} → {record['price']}")

            time.sleep(REFRESH_INTERVAL)

        except KeyboardInterrupt:
            print("\nStopping ingestion...")
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(10)


# -------------------------------
# Entry point
# -------------------------------
if __name__ == "__main__":
    stream_stock_data()

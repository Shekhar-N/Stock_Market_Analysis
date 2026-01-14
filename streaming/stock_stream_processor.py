from pyspark.sql.functions import col, to_timestamp, window, avg
from streaming.spark_session import get_spark_session

RAW_PATH = "data/raw/stock_stream"
OUTPUT_PATH = "data/processed/indicators"
CHECKPOINT_PATH = "data/checkpoints/stock_stream"

spark = get_spark_session()

# Read streaming JSON files
df = spark.readStream.schema(
    "symbol STRING, price DOUBLE, open DOUBLE, high DOUBLE, low DOUBLE, "
    "volume LONG, currency STRING, event_time STRING"
).json(RAW_PATH)

df = df.withColumn("event_time", to_timestamp(col("event_time")))

# 5-minute moving average
agg_df = df.groupBy(window(col("event_time"), "5 minutes"), col("symbol")).agg(
    avg("price").alias("avg_price")
)

query = (
    agg_df.writeStream.format("parquet")
    .option("path", OUTPUT_PATH)
    .option("checkpointLocation", CHECKPOINT_PATH)
    .outputMode("append")
    .start()
)

query.awaitTermination()

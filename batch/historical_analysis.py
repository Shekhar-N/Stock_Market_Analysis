from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("HistoricalAnalysis").getOrCreate()

df = spark.read.parquet("data/processed/indicators")
df.show()

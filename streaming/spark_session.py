from pyspark.sql import SparkSession


def get_spark_session(app_name="StockStreamingApp"):
    return (
        SparkSession.builder.appName(app_name)
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "2")
        .getOrCreate()
    )

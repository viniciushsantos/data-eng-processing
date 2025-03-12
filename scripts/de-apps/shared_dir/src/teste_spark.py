from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HelloPySpark") \
    .getOrCreate()

data = [("Testing local Spark",)]
columns = ["Message"]

df = spark.createDataFrame(data, columns)

print("==== TESTING SPARK ON K8S ====")

print(df.show())
spark.stop()
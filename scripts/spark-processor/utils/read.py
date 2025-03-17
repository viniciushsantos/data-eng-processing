from spark_session import SparkSessionManager
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType, StructType, StructField
from pb import flow_pb2
import base64

class read:
    """
    Author:        Vinícius Henrique dos Santos
    Date:          13/05/2025
    Description:   This class has the main goal of reading data from a source
    """
    def __init__(self, kafka_broker: str):
        """
        Inicializa a classe de leitura do Kafka.

        :param kafka_broker: The Kafka's server address (ex: "45.167.239.32:9092").
        """
        self.kafka_broker = kafka_broker
        self.spark = SparkSessionManager.spark_setup()

    def read_kafka(self, topic: str):
        """
        It reads data from Kafka topic and return into a Spark DataFrame.

        :param topic: Topic name to be consumed.
        :return: DataFrame do Spark with .
        """
        df = self.spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", self.kafka_broker) \
            .option("subscribe", topic) \
            .option("startingOffsets", "latest") \
            .load()

        return df.selectExpr("CAST(value AS STRING) as message")

    def stop_spark(self):
        """Finishes the SparkSession."""
        self.spark.stop()

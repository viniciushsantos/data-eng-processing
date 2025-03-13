from pyspark.sql import SparkSession
from pyspark import SparkConf

class SparkSessionManager:
    _spark = None 

    @classmethod
    def spark_setup(cls):

        if cls._spark is None:
            spark_jars = "/opt/spark/spark-processor/utils/jars/*"  

            conf = (
                SparkConf()
                .set("spark.sql.repl.eagerEval.enabled", "false")
                .set("spark.sql.execution.arrow.pyspark.enabled", "true")
                .set("spark.sql.session.timeZone", "UTC")
                .set("spark.network.timeout", "100000000")
                .set("spark.executor.heartbeatInterval", "100000000")
                .set("spark.memory.offHeap.enabled", "true")
                .set("spark.memory.offHeap.size", "4G")
                .set("spark.sql.autoBroadcastJoinThreshold", "0")
                .set("spark.sql.broadcastTimeout", "300000")
                .set("spark.kryoserializer.buffer.max", "2047m")
                .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
                .set("spark.jars", spark_jars)
                .set("spark.ui.showConsoleProgress", "true")
                .set("spark.logConf", "true")
                .set("spark.driver.bindAddress", "0.0.0.0")
            )

            cls._spark = SparkSession.builder \
                .appName("spark") \
                .config(conf=conf) \
                .getOrCreate()

        return cls._spark

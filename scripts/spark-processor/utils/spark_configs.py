from pyspark.sql import SparkSession
from pyspark import SparkConf


def spark_configs():

    """
    Author:         Vinícius Henrique dos Santos 
    Date:           12/05/2025
    Description:    This class has the main goal of configuring the SparkSesion with a batter performance for streaming
    """

    #setting spark configs
    spark_jars = '''
        /opt/spark/de-apps/shared_dir/jars/spark-sql-kafka-0-10_2.12-3.5.0.jar
    '''

    conf = (
            SparkConf()
            #.set("spark.kubernetes.container.image", "viniciusdossantos21/flow-processor:0.0.3")
            #.set("spark.kubernetes.namespace", "default")
            .set('spark.sql.repl.eagerEval.enabled', False)
            .set('spark.sql.execution.arrow.pyspark.enabled', True)
            .set('spark.sql.session.timeZone', 'UTC')
            .set('spark.network.timeout', '100000000')
            .set('spark.executor.heartbeatInterval', '100000000')
            #.set('spark.executor.memory', '16G') 
            #.set('spark.driver.memory', '48G') 
            #.set('spark.executor.memory', '1G') 
            #.set('spark.driver.memory', '2G') 
            #.set('spark.driver.maxResultSize', '2G')
            .set('spark.memory.offHeap.enabled', 'true')
            .set('spark.memory.offHeap.size', '4G' )
            .set('spark.sql.autoBroadcastJoinThreshold', '0') #Quando necessário forçar o Broadcast usando broadcast(df)
            .set('spark.sql.broadcastTimeout', '300000')  
            .set('spark.kryoserializer.buffer.max', '2047m') 
            #.set('spark.kryoserializer.buffer.max', 2047)
            .set('spark.serializer', 'org.apache.spark.serializer.KryoSerializer') 
            .set('spark.jars', spark_jars)
            .set('spark.ui.showConsoleProgress', True)
            .set('spark.logConf', True)
            .set('spark.driver.bindAddress', '0.0.0.0')
        )

    spark = (
            SparkSession
            .builder
            .config(conf=conf)
            #.config("spark.jars.packages", "io.delta:delta-core_2.12:2.0.2")
            .master('local[*]')
            .appName('PySpark')
            .getOrCreate()
        )
    return spark
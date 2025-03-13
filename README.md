python3 -m venv venv 
source venv/bin/activate
brew install openjdk@11

docker build -t viniciusdossantos21/flow-processor:0.0.3 .
docker push viniciusdossantos21/flow-processor:0.0.3
docker run --rm -it viniciusdossantos21/flow-processor:0.0.3 bash

/opt/spark/bin/spark-submit src/teste_spark.py

kubectl delete sparkapplications --all -n default
kubectl apply -f k8s/processor/spark-flows.yaml
kubectl logs spark-teste-python-driver -n default


Spark Version 3.5.3
Kafka Version 3.9.0
Connector Version org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0
Link: https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.0/
JAR name spark-sql-kafka-0-10_2.12-3.5.0.jar

export PYTHONPATH="/Users/viniciussantos/Documents/GitHub/data-eng-processing/scripts/de-apps:$PYTHONPATH"  
echo $PYTHONPATH 
python3 teste_spark.py
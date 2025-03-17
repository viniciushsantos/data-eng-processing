FROM spark:3.5.3

WORKDIR /opt/spark/
#ENV PYTHONPATH="/opt/spark/de-apps/app"
USER root  
RUN apt-get update && apt-get install -y nano && rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH=/opt/spark/spark-processor
RUN echo "export PYTHONPATH=/opt/spark/spark-processor" >> /root/.bashrc
RUN pip install --no-cache-dir protobuf

USER spark 

COPY scripts/ /opt/spark/
    
CMD ["bash"]


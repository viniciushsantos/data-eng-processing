FROM spark:3.5.3

WORKDIR /opt/spark/
COPY scripts/ /opt/spark/
CMD ["bash"]
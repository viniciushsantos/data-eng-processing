from utils.spark_session import SparkSessionManager

class SparkJob:
    def __init__(self):
        self.spark = SparkSessionManager.spark_setup()

    def run(self):
        print("#" * 110)
        print("==== TESTING SPARK ON K8S ====")
        print("#" * 110)

if __name__ == "__main__":
    job = SparkJob()
    job.run()


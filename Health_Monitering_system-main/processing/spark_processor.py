# processing/spark_processor.py
from pyspark.sql import SparkSession
from config import PATIENT_DATA_FILE

def process_data_with_spark(data_file):
    spark = SparkSession.builder.appName("HealthDataProcessing").getOrCreate()
    df = spark.read.csv(data_file, header=True, inferSchema=True)

    # Example: Calculate average BP
    average_bp = df.agg({"bp": "avg"}).collect()[0][0]
    print(f"Average Blood Pressure: {average_bp}")

    # Example: Identify patients with high cholesterol (you'll need to define what "high" is)
    high_cholesterol_patients = df.filter(df.cholesterol > 240) #Example Threshold
    high_cholesterol_patients.show()

    spark.stop()

if __name__ == '__main__':
    process_data_with_spark("../" + PATIENT_DATA_FILE) # Read data relative to root

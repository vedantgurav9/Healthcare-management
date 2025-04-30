# main.py
from data_generation import patient_data_generator
from processing import spark_processor
from analysis import data_analyzer
from dashboard import dashboard
from config import NUM_PATIENTS, PATIENT_DATA_FILE
import os

if __name__ == "__main__":

    # 1. Generate Patient Data
    if not os.path.exists("data"):
        os.makedirs("data")
    patient_data = patient_data_generator.generate_patient_data(NUM_PATIENTS)
    patient_data.to_csv(PATIENT_DATA_FILE, index=False)
    print("Patient data generated and saved.")

    # 2. Process Data with Spark
    print("Processing data with Spark...")
    spark_processor.process_data_with_spark(PATIENT_DATA_FILE)

    # 3. Analyze Data
    print("Analyzing data...")
    data_analyzer.analyze_data(PATIENT_DATA_FILE)

    # 4. Create Dashboard
    print("Creating dashboard...")
    dashboard.create_dashboard(PATIENT_DATA_FILE)

    print("Health Monitoring System workflow complete.")

# data_generation/patient_data_generator.py
from faker import Faker
import pandas as pd
import random
from config import NUM_PATIENTS # Import configuration
import os

def generate_patient_data(num_patients):
    fake = Faker()
    patient_ids = range(1, num_patients + 1)
    names = [fake.name() for _ in range(num_patients)]
    ages = [random.randint(18, 85) for _ in range(num_patients)]
    genders = [random.choice(['Male', 'Female']) for _ in range(num_patients)]
    contacts = [fake.phone_number() for _ in range(num_patients)]
    medical_histories = [fake.sentence(nb_words=6) for _ in range(num_patients)]

    # Generate health parameters
    bps = [random.randint(90, 160) for _ in range(num_patients)]  # Simulate BP
    sugar_levels = [random.randint(70, 200) for _ in range(num_patients)]
    cholesterols = [random.randint(120, 300) for _ in range(num_patients)]
    hemoglobins = [round(random.uniform(10.0, 18.0), 1) for _ in range(num_patients)]

    data = {
        'patient_id': patient_ids,
        'name': names,
        'age': ages,
        'gender': genders,
        'contact': contacts,
        'medical_history': medical_histories,
        'bp': bps,
        'sugar_level': sugar_levels,
        'cholesterol': cholesterols,
        'hemoglobin': hemoglobins
    }
    df = pd.DataFrame(data)
    return df

if __name__ == '__main__':
    #This will create a "data" directory if it doesn't exist already
    if not os.path.exists("data"):
        os.makedirs("data")

    patient_data = generate_patient_data(NUM_PATIENTS)
    patient_data.to_csv("../data/patient_data.csv", index=False)  #Save relative to the root directory
    print("Patient data generated and saved to data/patient_data.csv")

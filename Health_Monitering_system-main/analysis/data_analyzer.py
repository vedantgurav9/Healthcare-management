# analysis/data_analyzer.py
import pandas as pd
from scipy import stats
from config import PATIENT_DATA_FILE # Import relative file path

def analyze_data(data_file):
    df = pd.read_csv(data_file)

    # Example: Calculate mean and standard deviation of age
    mean_age = df['age'].mean()
    std_age = df['age'].std()
    print(f"Mean Age: {mean_age}, Standard Deviation: {std_age}")

    # Example: Correlation between age and cholesterol (example)
    correlation = df['age'].corr(df['cholesterol'])
    print(f"Correlation between Age and Cholesterol: {correlation}")

if __name__ == '__main__':
    analyze_data("../" + PATIENT_DATA_FILE) # Read data relative to root

# dashboard/dashboard.py
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from config import PATIENT_DATA_FILE

def create_dashboard(data_file):
    df = pd.read_csv(data_file)

    # 1. Histograms for Health Parameters
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot
    sns.histplot(df['bp'], kde=True)
    plt.title("Blood Pressure Distribution")

    plt.subplot(2, 2, 2)
    sns.histplot(df['sugar_level'], kde=True)
    plt.title("Sugar Level Distribution")

    plt.subplot(2, 2, 3)
    sns.histplot(df['cholesterol'], kde=True)
    plt.title("Cholesterol Distribution")

    plt.subplot(2, 2, 4)
    sns.histplot(df['hemoglobin'], kde=True)
    plt.title("Hemoglobin Distribution")

    plt.tight_layout()  # Adjust subplot parameters for a tight layout
    plt.savefig("health_parameter_distributions.png")
    print("Dashboard visualizations created (health_parameter_distributions.png)")


    # 2. Scatter Plots
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.scatterplot(x='age', y='cholesterol', data=df)
    plt.title("Age vs. Cholesterol")

    plt.subplot(1, 2, 2)
    sns.scatterplot(x='bp', y='sugar_level', data=df)
    plt.title("BP vs. Sugar Level")

    plt.tight_layout()
    plt.savefig("age_cholesterol_bp_sugar.png")
    print("Dashboard visualizations created (age_cholesterol_bp_sugar.png)")



    # 3. Box Plot of BP by Gender
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='gender', y='bp', data=df)
    plt.xlabel("Gender")
    plt.ylabel("Blood Pressure")
    plt.title("Blood Pressure Distribution by Gender")
    plt.savefig("bp_by_gender.png")
    print("Dashboard visualizations created (bp_by_gender.png)")


    # 4. Correlation Heatmap
    correlation_matrix = df[['age', 'bp', 'sugar_level', 'cholesterol', 'hemoglobin']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap of Health Parameters")
    plt.savefig("correlation_heatmap.png")
    print("Dashboard visualizations created (correlation_heatmap.png)")




if __name__ == '__main__':
    create_dashboard("../" + PATIENT_DATA_FILE)

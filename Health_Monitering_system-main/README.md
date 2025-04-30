# Health Monitoring System for Diagnostic Centers

## 📌 Project Overview

This project aims to develop a **Health Monitoring System** that analyzes patient health parameters such as **Blood Pressure, Sugar Level, Cholesterol, and Hemoglobin**. The system leverages **big data technologies** (Apache Spark, Hadoop) for efficient processing and **data visualization** to identify trends and potential health risks.

## 🚀 Features

- **Synthetic Patient Data Generation** (10,000 patient records)
- **Big Data Processing** using Apache Spark & Pandas
- **Statistical Analysis** (Mean, Standard Deviation, Correlation)
- **Data Visualization Dashboard** (Matplotlib, Seaborn)
- **Identification of High-Risk Patients**
- **Scalable for Real-World Integration**

## 🛠 Tech Stack

- **Programming Language:** Python (Pandas, NumPy, SciPy, Matplotlib, Seaborn)
- **Big Data Frameworks:** Apache Spark, Hadoop (Optional for distributed storage)
- **Data Generation:** Faker Library (Synthetic data simulation)
- **Visualization Tools:** Matplotlib, Seaborn

## 📂 Project Structure

```
├── data/                   # Sample patient dataset (CSV format)
├── src/                    # Source code for data processing & analysis
│   ├── data_generator.py    # Generates synthetic patient data
│   ├── data_processing.py   # Data cleaning, transformation, and Spark processing
│   ├── analysis.py          # Statistical analysis & health risk identification
│   ├── visualization.py     # Dashboard & data visualization
├── notebooks/              # Jupyter Notebooks for testing
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

## 📊 Data Generation

The dataset includes **10,000 synthetic patient profiles**, each with the following attributes:

- **Patient ID** (Unique Identifier)
- **Name, Age, Gender, Contact Information**
- **Medical History**
- **Blood Pressure (BP), Sugar Level, Cholesterol, Hemoglobin**

## 🔍 Data Processing Workflow

1. **Load Dataset**: Import CSV into Apache Spark DataFrame
2. **Data Cleaning**: Handle missing values, remove duplicates, and normalize health parameters
3. **Aggregation**: Compute mean, standard deviation, and statistical distributions
4. **Health Risk Identification**: Flag patients with abnormal health parameters

## 📈 Data Visualization

- **Histograms**: Distribution of BP, Sugar, Cholesterol, Hemoglobin
- **Scatter Plots**: Identifying relationships (e.g., Age vs. Cholesterol)
- **Box Plots**: Comparing BP across gender
- **Correlation Heatmap**: Relationships between all health parameters

## 🔮 Future Enhancements

- **Machine Learning Models** for disease prediction (Diabetes, Hypertension, etc.)
- **Real-Time Data Monitoring** using IoT & streaming pipelines (Kafka, Spark Streaming)
- **Integration with Wearable Devices** for continuous health tracking

## 🛠 Setup & Installation

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/juned-k786/health-monitoring-system.git
cd health-monitoring-syste
```

### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Data Generator**

```bash
python src/data_generator.py
```

### **4️⃣ Process Data using Spark**

```bash
python src/data_processing.py
```

### **5️⃣ Run the Dashboard**

```bash
python src/visualization.py
```

## 📜 License

This project is open-source and available under the **MIT License**.

---

💡 **Contributions are welcome!** Feel free to open issues and submit pull requests. 🚀

This project is open-source and available under the **MIT License**.

© 2025 Mohd Juned Khan. All rights reserved.


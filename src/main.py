import pandas as pd

# Load dataset
df = pd.read_csv("data/StudentPerformanceFactors.csv")

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("\nFirst 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nTarget Variable Statistics:")
print(df["Exam_Score"].describe())
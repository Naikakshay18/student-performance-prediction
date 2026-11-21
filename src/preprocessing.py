import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/StudentPerformanceFactors.csv")

print("Original Shape:", df.shape)

# -----------------------------
# Handle Missing Values
# -----------------------------

# Numerical columns
numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in numerical_cols:
    df[col] = df[col].fillna(df[col].median())

# Categorical columns
categorical_cols = df.select_dtypes(include=["object"]).columns

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -----------------------------
# Encode Categorical Columns
# -----------------------------

encoders = {}

for col in categorical_cols:
    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(df[col])

    encoders[col] = encoder

# -----------------------------
# Save Encoders
# -----------------------------
joblib.dump(encoders, "models/label_encoders.pkl")

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
df.to_csv("data/cleaned_student_data.csv", index=False)

print("\nProcessed Dataset:")
print(df.head())

print("\n✅ Cleaned dataset saved as:")
print("data/cleaned_student_data.csv")

print("\n✅ Label encoders saved as:")
print("models/label_encoders.pkl")
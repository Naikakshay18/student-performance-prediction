import pandas as pd

df = pd.read_csv("data/StudentPerformanceFactors.csv")

for col in df.select_dtypes(include="object").columns:
    print("\n" + col)
    print(df[col].dropna().unique())
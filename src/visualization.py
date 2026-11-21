import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/StudentPerformanceFactors.csv")

plt.figure(figsize=(8,5))
plt.hist(df["Exam_Score"], bins=20)

plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Students")

plt.show()
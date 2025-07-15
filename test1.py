import pandas as pd
import matplotlib.pyplot as plt

file_path = "API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv"
df = pd.read_csv(file_path, skiprows=4)

pop_2024 = df[["Country Name", "2024"]].dropna()

top_15 = pop_2024.sort_values("2024", ascending=False).head(15)

plt.figure(figsize=(12, 6))
plt.bar(top_15["Country Name"], top_15["2024"], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title("Top 15 Most Populous Countries in 2024")
plt.xlabel("Country")
plt.ylabel("Population")
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

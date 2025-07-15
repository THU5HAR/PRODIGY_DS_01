import pandas as pd
import matplotlib.pyplot as plt

pop_df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)
meta_df = pd.read_csv("Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv")

pop_2024 = pop_df[["Country Name", "Country Code", "2024"]].dropna()
merged = pd.merge(pop_2024, meta_df, on="Country Code")

grouped = merged.groupby("IncomeGroup")["2024"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
grouped.plot(kind='bar', color='mediumseagreen')
plt.title("Total Population in 2024 by Income Group")
plt.xlabel("Income Group")
plt.ylabel("Total Population")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

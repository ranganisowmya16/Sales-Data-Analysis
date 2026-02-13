import pandas as pd

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

# Show first 5 rows
print(df.head())
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())
print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum())

print("\nProfit by Category:")
print(df.groupby("Category")["Profit"].sum())

print("\nTop 5 States by Profit:")
print(df.groupby("State")["Profit"].sum().sort_values(ascending=False).head())
import matplotlib.pyplot as plt
# Sales by Category Graph
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Total Sales")
plt.show()

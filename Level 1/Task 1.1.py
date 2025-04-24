import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;sns.set(color_codes=True)

df = pd.read_csv(r"C:\Users\anjal\OneDrive\Desktop\CODES\Cognifyz DS Internship\Dataset.csv")

#1.Explore the dataset and identify the number of rows and columns.
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("Missing values in each column:\n")
print(df.isnull().sum())
df['Cuisines'].fillna('Unknown', inplace=True)
df.info()

# Count values
rating_counts = df['Aggregate rating'].value_counts().sort_index()

# Plot distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="viridis")
plt.title("Distribution of Aggregate Rating")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Print counts for reference
print(rating_counts)
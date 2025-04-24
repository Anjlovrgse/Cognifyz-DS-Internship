#import modules and dataset

import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;sns.set(color_codes=True)
df = pd.read_csv(r"C:\Users\anjal\OneDrive\Desktop\CODES\Cognifyz DS Internship\Dataset.csv")


most_common_price_range = df['Price range'].value_counts().idxmax()
print(f"Most Common Price Range: {most_common_price_range}")

avg_rating_by_price = df.groupby('Price range')['Aggregate rating'].mean().sort_index()
print("Average Rating by Price Range:\n", avg_rating_by_price)

# Group by Price range and Rating color, then calculate average rating
color_rating_by_price = df.groupby(['Price range', 'Rating color'])['Aggregate rating'].mean().reset_index()

# For each price range, find the color with highest average rating
top_color_by_price = color_rating_by_price.sort_values(['Price range', 'Aggregate rating'], ascending=[True, False]).drop_duplicates('Price range')
print("Top Rating Color by Price Range:\n", top_color_by_price[['Price range', 'Rating color', 'Aggregate rating']])


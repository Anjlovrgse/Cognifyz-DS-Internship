#import modules and dataset

import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;sns.set(color_codes=True)


df = pd.read_csv(r"C:\Users\anjal\OneDrive\Desktop\CODES\Cognifyz DS Internship\Dataset.csv")

# Total number of restaurants
total = len(df)

# Table booking
table_booking_pct = (df['Has Table booking'].str.lower() == 'yes').sum() / total * 100

# Online delivery
online_delivery_pct = (df['Has Online delivery'].str.lower() == 'yes').sum() / total * 100

print(f"📅 Table Booking Available: {table_booking_pct:.2f}%")
print(f"📦 Online Delivery Available: {online_delivery_pct:.2f}%")

# Convert to lowercase for consistency
df['Has Table booking'] = df['Has Table booking'].str.lower()

# Group by table booking status
rating_comparison = df.groupby('Has Table booking')['Aggregate rating'].mean()
print("📊 Average Ratings by Table Booking Availability:\n", rating_comparison)

# Normalize Online Delivery column
df['Has Online delivery'] = df['Has Online delivery'].str.lower()

# Count of online delivery availability across price ranges
online_by_price = df.groupby(['Price range', 'Has Online delivery']).size().unstack().fillna(0)

# Optional: Convert to percentage
online_by_price_pct = (online_by_price.T / online_by_price.sum(axis=1)).T * 100

print("📦 Online Delivery Distribution by Price Range:\n", online_by_price)
print("\n(%) Online Delivery Percentage by Price Range:\n", online_by_price_pct)


import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;sns.set(color_codes=True)

df = pd.read_csv(r"C:\Users\anjal\OneDrive\Desktop\CODES\Cognifyz DS Internship\Dataset.csv")

import numpy as np
# Mean
print("Means:\n", df.mean(numeric_only=True))
# Median
print("\nMedians:\n", df.median(numeric_only=True))
# Standard Deviation
print("\nStandard Deviations:\n", df.std(numeric_only=True))


#Country code
print("Country Code Distribution:\n")
print(df['Country Code'].value_counts())
df['Country Code'].value_counts().head(10).plot(kind='bar', figsize=(8, 5), title='Top Country Codes')
#City
print("\nCity Distribution:\n")
print(df['City'].value_counts())
df['City'].value_counts().head(10).plot(kind='bar', figsize=(10, 5), title='Top 10 Cities with Restaurants')
#Cuisines
print("\nCuisines Distribution:\n")
print(df['Cuisines'].value_counts())
df['Cuisines'].value_counts().head(10).plot(kind='bar', figsize=(10, 5), title='Top 10 Cuisines')


#Top Cuisines
top_cuisines = df['Cuisines'].value_counts().head(10)
print("Top 10 Cuisines:\n", top_cuisines)
top_cuisines.plot(kind='barh', figsize=(8, 5), title='Top 10 Cuisines')
#Top Cities with Most Restaurants
top_cities = df['City'].value_counts().head(10)
print("\nTop 10 Cities:\n", top_cities)
top_cities.plot(kind='barh', figsize=(8, 5), title='Top 10 Cities by Restaurant Count')

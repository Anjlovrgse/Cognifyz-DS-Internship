#import modules and dataset

import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;sns.set(color_codes=True)


df = pd.read_csv(r"C:\Users\anjal\OneDrive\Desktop\CODES\Cognifyz DS Internship\Dataset.csv")

import folium
from folium.plugins import MarkerCluster


map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=2)


marker_cluster = MarkerCluster().add_to(restaurant_map)


for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Restaurant Name']
    ).add_to(marker_cluster)


restaurant_map

#By City
city_dist = df['City'].value_counts()
print("Top 10 Cities with Most Restaurants:\n", city_dist.head(10))


city_dist.head(10).plot(kind='barh', title='Top 10 Cities by Restaurant Count')

#By Country
country_map = {
    1: "India", 14: "Australia", 30: "Brazil", 37: "Canada", 94: "Indonesia", 
    148: "New Zealand", 162: "Philippines", 166: "Qatar", 184: "Singapore", 
    189: "South Africa", 191: "Sri Lanka", 208: "Turkey", 214: "UAE", 
    215: "United Kingdom", 216: "United States"
}

df['Country'] = df['Country Code'].map(country_map)
country_dist = df['Country'].value_counts()
print("\nRestaurant Count by Country:\n", country_dist)


country_dist.plot(kind='bar', title='Restaurant Distribution by Country', figsize=(10,5))

# A. Use a scatter plot to visualize:
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Longitude', y='Latitude', hue='Aggregate rating', data=df, palette='coolwarm')
plt.title("Restaurant Locations Colored by Rating")
plt.show()
# B. Or calculate correlation:
correlations = df[['Latitude', 'Longitude', 'Aggregate rating']].corr()
print("Correlation Matrix:\n", correlations)
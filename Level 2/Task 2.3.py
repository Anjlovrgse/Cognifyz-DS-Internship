import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;sns.set(color_codes=True)
df = pd.read_csv(r"C:\Users\anjal\OneDrive\Desktop\CODES\Cognifyz DS Internship\Dataset.csv")

# Extract additional features
df['Restaurant Name Length'] = df['Restaurant Name'].apply(len)
df['Address Word Count'] = df['Address'].apply(lambda x: len(str(x).split()))

# Show outputs
df[['Restaurant Name', 'Restaurant Name Length', 'Address', 'Address Word Count',
    'Has Table booking', 'Has_Table_Booking_Flag',
    'Has Online delivery', 'Has_Online_Delivery_Flag']].head(10)


# Convert 'Yes' to 1 and 'No' to 0
df['Has_Table_Booking_Flag'] = df['Has Table booking'].str.lower().map({'yes': 1, 'no': 0})
df['Has_Online_Delivery_Flag'] = df['Has Online delivery'].str.lower().map({'yes': 1, 'no': 0})

# Print the updated DataFrame
print(df[['Has Table booking', 'Has_Table_Booking_Flag', 'Has Online delivery', 'Has_Online_Delivery_Flag']])
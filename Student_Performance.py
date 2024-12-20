import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('Cleaned_Students_Performance.csv')

# Define performance levels based on average_score
conditions = [
    (data['average_score'] >= 80),
    (data['average_score'] >= 60) & (data['average_score'] < 80),
    (data['average_score'] < 60)
]
performance_levels = ['High', 'Medium', 'Low']

# Ensure performance_levels is treated as an object (string type) array
data['performance_level'] = np.select(conditions, performance_levels, default='Unknown')

# Save cleaned data for use in the next step
data.to_csv('Curated_Students_Performance.csv', index=False)

import os
import pandas as pd

# path of the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'sierraleone-bumbuna.csv')

# Load the CSV file
df = pd.read_csv(csv_file_path)

# Perform data preparation steps
# ...

# Store the processed data in a variable 
processed_data = df
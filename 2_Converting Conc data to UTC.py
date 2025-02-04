# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:47:13 2025

@author: lb945465
"""

import pandas as pd
from pytz import timezone

# File paths
file_paths = [
    r"C:\Users\LB945465\Desktop\Trajectories\Bronx_PAMS.csv",
    r"C:\Users\LB945465\Desktop\Trajectories\Bronx_canister.csv"
]

# Function to convert date column from EST to UTC
def convert_est_to_utc(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Convert the 'Date' column to datetime and set timezone to EST
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.tz_localize('America/New_York', ambiguous='NaT', nonexistent='shift_forward')
    
    # Convert to UTC
    df['Date'] = df['Date'].dt.tz_convert('UTC')
    
    # Save the updated file
    updated_file_path = file_path.replace(".csv", "_UTC.csv")
    df.to_csv(updated_file_path, index=False)
    print(f"Updated file saved to: {updated_file_path}")

# Process each file
for path in file_paths:
    convert_est_to_utc(path)

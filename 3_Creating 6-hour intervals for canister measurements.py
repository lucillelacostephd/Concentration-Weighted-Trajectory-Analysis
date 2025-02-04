# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:46:34 2025
Creating 6-hour intervals for canister measurements
@author: lb945465
"""

import pandas as pd

# Load data
file_path = r"C:\Users\LB945465\Desktop\Trajectories\Bronx_canister_UTC.csv"
canister_data = pd.read_csv(file_path)

# Convert 'Date' column to datetime
canister_data['Date'] = pd.to_datetime(canister_data['Date'])

# Expand to 6-hour intervals across all columns
expanded_data = pd.concat(
    [
        canister_data.assign(Date=canister_data['Date'] + pd.Timedelta(hours=hours))
        for hours in [0, 6, 12, 18]
    ]
)

# Sort by date and reset index
expanded_data = expanded_data.sort_values('Date').reset_index(drop=True)

# Save the output
output_path = r"C:\Users\LB945465\Desktop\Trajectories\Bronx_6_hourly_canister.csv"
expanded_data.to_csv(output_path, index=False)

print(f"6-hour expanded data successfully saved to {output_path}")

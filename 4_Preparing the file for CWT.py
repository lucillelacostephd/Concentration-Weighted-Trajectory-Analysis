# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 08:50:08 2025

@author: lb945465
"""

import pandas as pd

# File paths
#conc_file = r"C:\Users\LB945465\Desktop\Trajectories\Bronx_PAMS_UTC.csv"
conc_file = r"C:\Users\LB945465\Desktop\Trajectories\Bronx_6_hourly_canister.csv"
traj_file = r"C:\Users\LB945465\Desktop\Trajectories\BronxTrajData.csv"

# Function to clean column names (replace spaces with underscores)
def clean_column_names(df):
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('-', '_')
    return df

# Function to read and clean a CSV file
def read_and_clean_csv(file_path):
    df = pd.read_csv(file_path)
    df = clean_column_names(df)
    return df

# Read and clean both datasets
conc_file = read_and_clean_csv(conc_file)
traj_data = read_and_clean_csv(traj_file)

# Convert 'Date' columns to datetime format
conc_file['Date'] = pd.to_datetime(conc_file['Date'])
traj_data['Date'] = pd.to_datetime(traj_data['date2'])

# Ensure both datasets have UTC-aware timestamps

# Localize PAMS data if needed
if conc_file['Date'].dt.tz is None:
    conc_file['Date'] = conc_file['Date'].dt.tz_localize('UTC')

# Localize trajectory data to UTC (assumes timestamps are already in UTC)
# traj_data['Date'] = traj_data['Date'].dt.tz_localize('UTC')

# Merge the datasets
merged_data = pd.merge(traj_data, conc_file, on='Date', how='inner')

# Save the merged data
merged_file_path = r"C:\Users\LB945465\Desktop\Trajectories\Merged_Traj_canister.csv"
merged_data.to_csv(merged_file_path, index=False)

print(f"Merged data saved to: {merged_file_path}")

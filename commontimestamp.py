# -*- coding: utf-8 -*-
"""CommonTimestamp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/121atsNwH4eqtR6loMQyxbmzG7WxSwJ-W
"""

!pip install nsepython

import pandas as pd

# File paths for the uploaded Excel files
file1_path = '/content/MEDIASSIST_MaxPeriod.csv'
file2_path = '/content/NSEI_MaxPeriod.csv'

# Read the Excel files
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Merge the dataframes based on the common 'CH_TIMESTAMP' column
merged_df = pd.merge(df1, df2, on='CH_TIMESTAMP')

# Save the merged dataframe to a new Excel file
output_file = 'commontimestamp_data.xlsx'
merged_df.to_excel(output_file, index=False)

print("Merged data has been saved to", output_file)
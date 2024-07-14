# Reading the CSV data
import pandas as pd
df = pd.read_csv("sample_projections.csv")

# Sorting the dataframe by 'relationships.league.data.type'
sorted_df = df.sort_values(by='relationships.league.data.id')

sorted_df.to_csv("sample_projections.csv", index=False)
import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(method='ffill')

print(df.head())
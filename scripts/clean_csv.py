import pandas as pd

# Load CSV without low-memory warning
df = pd.read_csv("data/nyc_311.csv", low_memory=False)

# Function to parse datetime safely
def parse_datetime(col):
    return pd.to_datetime(col, format='%m/%d/%Y %I:%M:%S %p', errors='coerce')

# Columns to convert
datetime_cols = ["Created Date", "Closed Date", "Due Date", "Resolution Action Updated Date"]

for col in datetime_cols:
    df[col] = parse_datetime(df[col])
    df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')

# Save cleaned CSV
df.to_csv("data/nyc_311_clean.csv", index=False)
print("CSV cleaned and saved as data/nyc_311_clean.csv")

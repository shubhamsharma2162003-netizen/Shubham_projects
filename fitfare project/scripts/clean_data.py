import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/source1_raw.csv")

print("Total rows before cleaning:", len(df))

# Remove duplicates
df.drop_duplicates(inplace=True)

print("Total rows after cleaning:", len(df))

# Save cleaned data
df.to_csv("cleaned/final_cleaned.csv", index=False)

df.to_excel("cleaned/final_cleaned.xlsx", index=False)

print("Cleaning completed successfully!")
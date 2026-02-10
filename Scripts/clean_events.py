import pandas as pd


df = pd.read_csv("data/raw_events.csv")

print("Original data shape:", df.shape)


print("\nMissing values per column:")
print(df.isnull().sum())


df = df.dropna()


df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")


df = df.dropna(subset=["timestamp"])


df["event_type"] = df["event_type"].str.lower().str.strip()
df["source"] = df["source"].str.lower().str.strip()


df["success"] = df["success"].astype(bool)

print("Cleaned data shape:", df.shape)


df.to_csv("data/clean_events.csv", index=False)

print("✅ Cleaned data saved to: data/clean_events.csv")
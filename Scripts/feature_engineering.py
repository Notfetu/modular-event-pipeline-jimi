import pandas as pd

# Load cleaned data
df = pd.read_csv("data/clean_events.csv")

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Create a date column
df["date"] = df["timestamp"].dt.date

# -------------------------------
# Feature Engineering
# -------------------------------

# Total number of events per user
event_count = df.groupby("user_id").size().rename("event_count")

# Success rate per user
success_rate = df.groupby("user_id")["success"].mean().rename("success_rate")

# Count of each event type per user
event_type_counts = df.pivot_table(
    index="user_id",
    columns="event_type",
    values="event_id",
    aggfunc="count",
    fill_value=0
)

# Number of active days per user
active_days = df.groupby("user_id")["date"].nunique().rename("active_days")

# Combine all features into one table
features = pd.concat(
    [event_count, success_rate, event_type_counts, active_days],
    axis=1
)

# Reset index so user_id becomes a column
features = features.reset_index()

# Save features
features.to_csv("data/user_features.csv", index=False)

print("✅ Feature engineering complete.")
print("✅ Features saved to: data/user_features.csv")
print("\nSample features:")
print(features.head())
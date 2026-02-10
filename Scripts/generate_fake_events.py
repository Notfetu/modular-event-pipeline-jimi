import pandas as pd
import uuid
import random
from datetime import datetime, timedelta


NUM_EVENTS = 500

event_types = ["login", "upload", "download", "logout"]
sources = ["web", "mobile", "api"]

events = []

start_time = datetime.now() - timedelta(days=7)

for _ in range(NUM_EVENTS):
    event = {
        "event_id": str(uuid.uuid4()),
        "event_type": random.choice(event_types),
        "timestamp": (start_time + timedelta(minutes=random.randint(0, 10000))).isoformat(),
        "user_id": f"user_{random.randint(1, 50)}",
        "source": random.choice(sources),
        "success": random.choice([True, True, True, False])  # mostly successful
    }
    events.append(event)

df = pd.DataFrame(events)

df.to_csv("data/raw_events.csv", index=False)

print("✅ Fake event data generated: data/raw_events.csv") 

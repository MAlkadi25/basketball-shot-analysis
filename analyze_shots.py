
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("shots_sample.csv")

# Clean data
df['make'] = (df['result'].str.lower() == 'make').astype(int)

# Distance buckets
def bucket(d):
    if d <= 3: return "0-3 ft"
    if d <= 10: return "3-10 ft"
    if d <= 16: return "10-16 ft"
    if d < 22: return "16-22 ft"
    return "3PT (22+ ft)"

df['distance_bucket'] = df['distance_ft'].apply(bucket)

# Overall FG%
overall = df['make'].mean() * 100
with open("summary_overall.txt","w") as f:
    f.write(f"Overall FG%: {overall:.1f}%\n")

# By distance
by_dist = df.groupby('distance_bucket')['make'].mean() * 100
by_dist.to_csv("summary_by_distance.csv")
by_dist.plot(kind='bar', title="FG% by Distance")
plt.ylabel("FG%")
plt.tight_layout()
plt.savefig("fg_by_distance.png")
plt.close()

# By location
by_loc = df.groupby('location')['make'].mean() * 100
by_loc.to_csv("summary_by_location.csv")
by_loc.plot(kind='bar', title="FG% by Location")
plt.ylabel("FG%")
plt.tight_layout()
plt.savefig("fg_by_location.png")
plt.close()

print("Analysis complete. Charts and summaries generated.")

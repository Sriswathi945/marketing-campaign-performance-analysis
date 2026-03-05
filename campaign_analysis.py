import pandas as pd

data = pd.read_csv("campaign_data.csv")

conversion_rate = data["conversions"].sum() / data["clicks"].sum()
print("Conversion Rate:", conversion_rate)

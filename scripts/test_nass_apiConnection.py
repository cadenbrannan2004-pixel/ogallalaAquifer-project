import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NASS_API_KEY")

if api_key is None:  # Checks to see if key is available
    raise SystemExit("No API Present.")

url = "https://quickstats.nass.usda.gov/api/get_counts/"

# Dictionary for data on cotton and its respective county
params = {
    "key": api_key,
    "source_desc": "SURVEY",
    "commodity_desc": "COTTON",
    "statisticcat_desc": "AREA HARVESTED",
    "agg_level_desc": "COUNTY",
    "state_alpha": "TX",
}

response = requests.get(
    url, params=params, timeout=60
)  # stops after 60 second if request fails
print("Status code:", response.status_code)
print(response.json())

if response.status_code == 200:
    print("Request was successful!")
else:
    print(f"Failed to retrieve data. Statust code: {response.status_code}")

# 'count': 15756

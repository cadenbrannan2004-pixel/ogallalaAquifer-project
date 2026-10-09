import os
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NASS_API_KEY")
if API_KEY is None:
    raise SystemExit("No API key present.")

BASE_URL = "https://quickstats.nass.usda.gov/api/api_GET/"
OUTPUT_PATH = Path("data/raw/nass_cotton_tx_county.csv")

params = {
    "key": API_KEY,
    "source_desc": "SURVEY",
    "commodity_desc": "COTTON",
    "statisticcat_desc": "AREA HARVESTED",
    "agg_level_desc": "COUNTY",
    "state_alpha": "TX",
}

response = requests.get(BASE_URL, params=params, timeout=120)
response.raise_for_status()

records = response.json()["data"]
df = pd.DataFrame(records)
print(f"Acquired {len(df):,} rows")

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)
print(f"Saved to {OUTPUT_PATH}")

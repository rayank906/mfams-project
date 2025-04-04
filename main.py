import requests
import pandas as pd
from io import StringIO

# Setting up API call to retrieve Kalshi data
api_url = "https://api.elections.kalshi.com/trade-api/v2/api_version"

headers = {"accept": "319b80cd-7ba7-40c2-ba22-4972bf48d75e"}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)
    print(df.head())
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
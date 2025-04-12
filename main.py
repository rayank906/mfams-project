import requests
import pandas as pd
from io import StringIO

# Setting up API call to retrieve Kalshi data
# api_url = "https://api.elections.kalshi.com/trade-api/v2/api_version"

# url = "https://api.elections.kalshi.com/trade-api/v2/markets/presidential-elections"

# headers = {"accept": "319b80cd-7ba7-40c2-ba22-4972bf48d75e"}

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     csv_data = StringIO(response.text)
#     df = pd.read_csv(csv_data)
#     print(df.head())
# else:
#     print(f"Failed to fetch data. Status Code: {response.status_code}")

url = "https://api.elections.kalshi.com/trade-api/v2/markets/presidential-elections"

headers = {
    "accept": "application/json",
    "Authorization": "319b80cd-7ba7-40c2-ba22-4972bf48d75e"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    df = pd.json_normalize(data['markets'])
    print(df.head())
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
    print("Response:", response.text)

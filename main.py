# import requests
# import pandas as pd
# from io import StringIO

# # Setting up API call to retrieve Kalshi data
# api_url = "https://api.elections.kalshi.com/trade-api/v2/api_version"

# headers = {"accept": "application/json"}

# response = requests.get(api_url, headers=headers)

# if response.status_code == 200:
#     csv_data = StringIO(response.text)
#     df = pd.read_csv(csv_data)
#     print(df.head())
# else:
#     print(f"Failed to fetch data. Status Code: {response.status_code}")

import requests

url = "https://api.elections.kalshi.com/trade-api/v2/api_version"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
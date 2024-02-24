from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "190c0d3122ef7a2c943c" #freecurrencyconverterapi.com

printer = PrettyPrinter()

def get_currency():
    endpoint = f"/api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    try:
        response = get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()['results']
        data = list(data.items())
        data.sort()
        return data
    except Exception as e:
        print("Error occurred:", e)
        return None
    
def print_currency(currencies):
    for j, i in currencies:
        curr_name = i['currencyName']
        curr_id = i['id']
        curr_symbol = i.get("currencySymbol","")
        print(f"{curr_id} - {curr_name} - {curr_symbol}")

data = get_currency()
if data is not None:
    print_currency(data)
else:
    print("Failed to fetch currency data.")

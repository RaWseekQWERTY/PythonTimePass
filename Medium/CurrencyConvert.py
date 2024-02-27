from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com"
API_KEY = "190c0d3122ef7a2c943c" #freecurrencyconverterapi.com

printer = PrettyPrinter()

def get_currency():
    endpoint = f"/api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    try:
        response = get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        Data = response.json()
        data = Data["results"]
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
def currency_exc_rate(currency1,currency2):
    endpoint = f"/api/v7/convert?q={currency1}_{currency2},{currency2}_{currency1}&compact=ultra&apiKey=[YOUR_API_KEY]"   
    url = BASE_URL+endpoint
    response = get(url)
    data = response.json()
    if len(data) == 0:
        print("Currency was not found")
        return
    return list(data.values())[0]

data = get_currency()
if data is not None:
    print_currency(data)
else:
    print("Failed to fetch currency data.")

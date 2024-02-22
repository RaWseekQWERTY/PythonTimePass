from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "190c0d3122ef7a2c943c" #freecurrencyconverterapi.com

printer = PrettyPrinter()

def get_currency():
    endpoint = f"api/v7/currencies?apikey={API_KEY}" # ?(query)
    url = BASE_URL + endpoint
    data = get(url).json()
    printer.pprint(data)
    
get_currency()
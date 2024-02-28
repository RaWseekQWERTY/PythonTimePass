from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com"
API_KEY = "YOUR_API_KEY" #freecurrencyconverterapi.com

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
    rate = list(data.values())[0]
    print(f"{currency1}->{currency2}={rate}")
    return rate

def convert_curr(currency1,currency2,amount):
    rate = currency_exc_rate(currency1,currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except Exception:
        print("Invalid amount")
        return
    converted_amt = rate * amount
    print(f"{amount} of {currency1} to {currency2} is equivalent to {converted_amt} {currency2}")
    return converted_amt

def main():
    currency = get_currency()
    print("Welcome to Currency Convert System")
    print("1 - list different currencies")
    print("2 - convert from one currency to another")
    print("3 - get exchnage rate of two currencies")
    print()
    while True:
        command = input("Enter a command (q to quit): \n").lower()
        if command == "q":
            break
        elif command == "1":
            print_currency(currency)
        elif command == "2":
            currency1 = input("Enter the first currency: \n").upper()
            currency2 = input("Enter the second currency: \n").upper()
            amount = input("Enter the amount: \n")
            convert_curr(currency1, currency2, amount)
        elif command == "3":
            currency1 = input("Enter a base currency: \n").upper()
            currency2 = input("Enter the second currency: \n").upper()
            currency_exc_rate(currency1, currency2)
        else:
            print("Unknown command: %s" )
            
    
main()
# data = get_currency()
# if data is not None:
#     print_currency(data)
# else:
#     print("Failed to fetch currency data.")

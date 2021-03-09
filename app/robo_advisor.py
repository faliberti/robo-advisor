# this is the "app/robo_advisor.py" file

import requests
import json
import os
import csv
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def to_usd(my_price):
    return f"${my_price:,.2f}"

API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY", "abc123")

symbol = input("Please input the symbol of stock(s) (e.g. TSLA).")
if symbol.isalpha() == False or len(symbol) > 5:
    print("There was an error with what you put. Please try again with a stock symbol. (e.g. TSLA)")
    exit()
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
response = requests.get(request_url)
if "Error Message" in response.text:
    print("Sorry there was an error and we found no trading data for that symbol.")
    exit()
parsed_response = json.loads(response.text)
def transform_response(parsed_response):
    trans = parsed_response['Time Series (Daily)']
    rows = []
    for date, daily_prices in trans.items():
        row = {
            'timestamp': date,
            "open price": float(daily_prices["1. open"]),
            "high": float(daily_prices["2. high"]),
            "low": float(daily_prices["3. low"]),
            "close price": float(daily_prices["4. close"]),
            "volume": int(daily_prices["5. volume"])
        }
        rows.append(row)

    return rows
print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
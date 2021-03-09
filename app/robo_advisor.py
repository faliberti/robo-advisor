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

present = datetime.now()

symbol = input("Please input the symbol of stock(s) (e.g. TSLA).")
if symbol.isalpha() == False or len(symbol) > 5:
    print("There was an error with what you put. Please run the advisor again with a stock symbol. (e.g. TSLA)")
    exit()
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
response = requests.get(request_url)
if "Error Message" in response.text:
    print("Sorry there was an error and we found no trading data for that symbol. Please run the advisor again.")
    exit()
parsed_response = json.loads(response.text)

tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys())

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close_price = tsd[dates[0]]["4. close"]

high_price = [float(tsd[date]["2. high"]) for date in dates]
low_price = [float(tsd[date]["3. low"]) for date in dates]

recent_high_price = max(high_price)
recent_low_price = min(low_price)

csv_file_path = os.path.join(os.path.dirname(__file__),"..", "data", "prices.csv")

with open(csv_file_path, "w") as csv_file: 
    writer = csv.DictWriter(csv_file, fieldnames=["timestamp", "open", "high", "low", "close", "volume"])
    writer.writeheader() 
    for date in dates:
        writer.writerow({
            "timestamp": date, 
            "open": tsd[date]["1. open"], 
            "high": tsd[date]["2. high"], 
            "low": tsd[date]["3. low"], 
            "close": tsd[date]["4. close"], 
            "volume": tsd[date]["5. volume"]
            })

recommend = "Do Not Buy"
reason = 'The most recent closing price was 25 percent above its most recent low.'

if float(latest_close_price) <= (1.25 * recent_low_price):
    recommend = "Buy"
    reason = "The most recent closing price is under 1.25x of the most recent low."


print("-------------------------")
print("SELECTED SYMBOL:", symbol.upper())
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:", present.strftime("%B %d, %Y at %I:%M %p"))
print("-------------------------")
print("LATEST DAY:", last_refreshed)
print("LATEST CLOSE", to_usd(float(latest_close_price)))
print("RECENT HIGH:", to_usd(recent_high_price))
print("RECENT LOW:", to_usd(recent_low_price))
print("-------------------------")
print("RECOMMENDATION:", recommend)
print("RECOMMENDATION REASON:", reason)
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
import cctx
from datetime import datetime
import json
import time

exchange = ccxt.binance()
money = 10000

bitcoin_1 = 0
bitcoin_2 = 0
bitcoin_3 = 0

while True:

    current_time = datetime.now().time()
    rounded_time = current_time.replace(second=0, microsecond=0)

    if rounded_time.strftime("%H:%M:%S") == "01:00:00":
        bitcoin_1 = float(exchange.fetch_ticker('BTC/USDT')["info"]["lastPrice"])

    if rounded_time.strftime("%H:%M:%S") == "02:00:00":
        bitcoin_2 = float(exchange.fetch_ticker('BTC/USDT')["info"]["lastPrice"])
    
    if rounded_time.strftime("%H:%M:%S") == "03:00:00":
        bitcoin_3 = float(exchange.fetch_ticker('BTC/USDT')["info"]["lastPrice"])
    
    if rounded_time.strftime("%H:%M:%S") == "04:00:00":

        current_price = float(exchange.fetch_ticker('BTC/USDT')["info"]["lastPrice"])

        money_1 = (bitcoin_1 / current_price) * money
        money_2 = (bitcoin_2 / current_price) * money
        money_3 = (bitcoin_3 / current_price) * money

        with open("bitcoin_1.json", "r") as f:
            data_1 = json.load(f)
        data_1.append(money_1)
        with open("bitcoin_1.json", "w") as f:
            json.dump(data_1, indent=4)
        
        with open("bitcoin_2.json", "r") as f:
            data_2 = json.load(f)
        data_2.append(money_2)
        with open("bitcoin_2.json", "w") as f:
            json.dump(data_2, indent=4)

        with open("bitcoin_3.json", "r") as f:
            data_3 = json.load(f)
        data_3.append(money_3)
        with open("bitcoin_3.json", "w") as f:
            json.dump(data_3, indent=4)
        
    time.sleep(20)


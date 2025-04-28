import json
import requests


from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('PKNN36CBNG3P86DVFZJW', '6xzltbPsztnlRdn3lk6prWoftf248MvmBbRMOtxl', paper=True)

def initial_data_pull(ticker):
    url = "http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&outputsize=full&apikey=NG9C9EPVYBMQT0C8"
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    lines = []
    
    with open("/home/ubuntu/data5500_mycode/final_project/data/" +ticker+ ".csv", "w") as file:
    
        for date in data["Time Series (Daily)"].keys():
            lines.append(date+", "+data["Time Series (Daily)"][date]["4. close"] +"\n")
            
        file.writelines(lines[::-1])
    
def append_data(ticker):
    #needs to pull from the API
    url = "http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&outputsize=full&apikey=NG9C9EPVYBMQT0C8"
    
    response = requests.get(url)
    data = json.loads(response.text)

    #needs to check the date from the API file
    with open("/home/ubuntu/data5500_mycode/final_project/data/" +ticker+ ".csv") as csv_file:
        csv_lines = csv_file.readlines()
        last_day = csv_lines[-1].split(",")[0]
        
    #compare data from the API and csv file
    new_lines = []
    
    with open("/home/ubuntu/data5500_mycode/final_project/data/" +ticker+ ".csv", "a") as file:
    
        for date in data["Time Series (Daily)"].keys():
            if date == last_day:
                break
            else:
                new_lines.append(date+", "+data["Time Series (Daily)"][date]["4. close"] +"\n")
            
        file.writelines(new_lines[::-1]) #needs to add everything "new"

        last_day = csv_lines[-1].split(",")[0].strip()


def meanReversionStrategy(prices): 
    rating_mr = 0 
    i = 0
    buy = 0
    sell = 0
    first_buy = 0
    total_profit = 0
    last_signal = "hold" #to track what the last buy/sell signal is
    
    for price in prices:
        current_price = prices[i]
        if i > 4:
            avg_price = (prices[i-1] + prices[i-2] + prices[i-3] + prices [i-4] + prices[i-5])/5

            # BUY logic (includes closing a short position)
            if current_price < avg_price * 0.98 and buy == 0:
                if sell != 0:  # closing short position
                    total_profit += sell - current_price
                    sell = 0
                buy = current_price
                if first_buy == 0:
                    first_buy = current_price

            # SELL logic (includes short selling)
            elif current_price > avg_price * 1.02 and buy != 0:
                total_profit += current_price - buy
                buy = 0
            elif current_price > avg_price * 1.02 and sell == 0 and buy == 0:
                sell = current_price
                if first_buy == 0:
                    first_buy = current_price
                    
        i += 1
        
    # If no action was taken on the last day, determine the last signal
    if last_signal == "hold":
        if prices[-1] > avg_price * 1.02:
            last_signal = "sell"
        elif prices[-1] < avg_price * 0.98:  
            last_signal = "buy"
        
    final_profit_percent = round((total_profit/first_buy) * 100, 2)
    total_profit = round(total_profit, 2)

    
    #    run strategy and output buys/sells, final profit, and final percentage returns
    print("Total Profit Value:", total_profit)
    print("First Buy:", first_buy)
    print("% return:", final_profit_percent, "%")
    #printing whether the stock should be bought, sold, or just held on the last day
    if last_signal == "buy":
        rating_mr = 1
    elif last_signal == "sell":
        rating_mr = -1
    else:
        rating_mr = 0
    print("Mean Reversion rating:", rating_mr)
        
    print("___________________") 
    
    returns = round((total_profit/first_buy) * 100, 2)
    return total_profit, returns, last_signal, rating_mr
    
def simpleMovingAverage(prices):
    rating_sma = 0
    i = 0
    buy = 0
    sell = 0  # for short selling
    first_trade_price = 0
    total_profit = 0
    last_signal = "hold"
    
    for price in prices:
        current_price = prices[i]
        if i > 4:
            avg_price = sum(prices[i-5:i]) / 5
            
            # Buy signal - includes closing a short position
            if current_price > avg_price and buy == 0:
                if sell != 0:
                    total_profit += sell - current_price
                    sell = 0
                buy = current_price
                if first_trade_price == 0:
                    first_trade_price = current_price
                if i == len(prices) - 1:
                    last_signal = "buy"
            
            # Sell signal - includes short selling
            elif current_price < avg_price:
                if buy != 0:
                    total_profit += current_price - buy
                    buy = 0
                    if i == len(prices) - 1:
                        last_signal = "sell"
                elif sell == 0:
                    sell = current_price
                    if first_trade_price == 0:
                        first_trade_price = current_price
                    if i == len(prices) - 1:
                        last_signal = "sell"
        i += 1

    # Check for signal on last day if no trades happened
    if last_signal == "hold":
        if prices[-1] < avg_price:
            last_signal = "sell"
        elif prices[-1] > avg_price:
            last_signal = "buy"

    final_profit_percent = round((total_profit / first_trade_price) * 100, 2) if first_trade_price != 0 else 0
    total_profit = round(total_profit, 2)

    print("Total Profit Value:", total_profit)
    print("First Trade Price:", first_trade_price)
    print("% return:", final_profit_percent, "%")
    if last_signal == "buy":
        rating_sma = 1
    elif last_signal == "sell":
        rating_sma = -1
    else:
        rating_sma = 0
    print("Simple Moving Average rating:", rating_sma)

    print("___________________") 

    
    return total_profit, final_profit_percent, last_signal, rating_sma

    
def bollingerBands(prices):
    rating_bb = 0
    i = 0
    buy = 0
    sell = 0  # for short selling
    first_trade_price = 0
    total_profit = 0
    last_signal = "hold"
    
    for price in prices:
        current_price = prices[i]
        if i > 4:
            avg_price = sum(prices[i-5:i]) / 5

            # Buy signal (above +5%) - includes closing a short
            if current_price > avg_price * 1.05 and buy == 0:
                if sell != 0:
                    total_profit += sell - current_price
                    sell = 0
                buy = current_price
                if first_trade_price == 0:
                    first_trade_price = current_price
                if i == len(prices) - 1:
                    last_signal = "buy"

            # Sell signal (below -5%) - includes short selling
            elif current_price < avg_price * 0.95:
                if buy != 0:
                    total_profit += current_price - buy
                    buy = 0
                    if i == len(prices) - 1:
                        last_signal = "sell"
                elif sell == 0:
                    sell = current_price
                    if first_trade_price == 0:
                        first_trade_price = current_price
                    if i == len(prices) - 1:
                        last_signal = "sell"
        i += 1

    # Last day signal fallback
    if last_signal == "hold":
        if prices[-1] < avg_price * 0.95:
            last_signal = "sell"
        elif prices[-1] > avg_price * 1.05:
            last_signal = "buy"

    final_profit_percent = round((total_profit / first_trade_price) * 100, 2) if first_trade_price != 0 else 0
    total_profit = round(total_profit, 2)

    print("Total Profit Value:", total_profit)
    print("First Trade Price:", first_trade_price)
    print("% return:", final_profit_percent, "%")
    if last_signal == "buy":
        rating_bb = 1
    elif last_signal == "sell":
        rating_bb = -1
    else:
        rating_bb = 0
    print("Bollinger Bands rating:", rating_bb)
    
    print("___________________") 
    
    return total_profit, final_profit_percent, last_signal, rating_bb


def saveResults(results):
    json.dump(results, open("/home/ubuntu/data5500_mycode/final_project/final_project.json", "w"), indent = 4)

def alpacaTrades(avg_rating, ticker):
    side = None

    if avg_rating > 0:
        print("You should BUY this stock today (avg rating is", avg_rating, ")")
        side = OrderSide.BUY
    elif avg_rating < 0:
        print("You should SELL this stock today (avg rating is", avg_rating, ")")
        side = OrderSide.SELL
    else:
        print("You should HOLD this stock today (avg rating is", avg_rating, ")")

    #preparing the order
    if side != None: #buy or sell if it is not a HOLD order
        market_order_data = MarketOrderRequest(
                        symbol= ticker,
                        qty=1,
                        side=side,
                        time_in_force=TimeInForce.DAY
                        )

        # Market order
        market_order = trading_client.submit_order(
                        order_data=market_order_data
                    )
        print("The status of the order is:", market_order.status)


tickers = ["GPRO", "AAPL", "GOOG", "COST", "AMZN", "DJT", "CVNA", "ADBE", "NVDA", "MSFT"] #pick my own 10 stocks i want to use
results = {}

#highest/best strategy/profit
most_profit = 0
best_strat = ""
best_ticker = ""

for ticker in tickers:
    # initial_data_pull(ticker) #I will only run this code once
    append_data(ticker) #This is the function that I should run each day.
    

    prices = [round(float(line.split(",")[1]), 2) for line in open("/home/ubuntu/data5500_mycode/final_project/data/"+ticker+".csv").readlines()]
    
    #call the output of each ticker in each strategy
    print("\n"+ticker, "Mean Reversion Strategy Output:")
    mr_profit, mr_returns, last_signal, rating_mr = meanReversionStrategy(prices)
    
    print("\n"+ticker, "Simple Moving Average Output:")
    sma_profit, sma_returns, last_signal, rating_sma = simpleMovingAverage(prices)
    
    print("\n"+ticker, "Bollinger Bands Output:")
    bb_profit, bb_returns, last_signal, rating_bb = bollingerBands(prices)

    #get the average of the 3 ratings to know if I should buy or sell in Alapca
    ratings = [rating_mr, rating_sma, rating_bb]
    avg_rating = sum(ratings) / len(ratings)
    alpacaTrades(avg_rating, ticker)
    

    #store the prices and the results of each strategy in a dictionary
    results[ticker+"_prices"] = prices 
    
    results[ticker+"_mr_profit"] = mr_profit
    results[ticker+"_mr_returns"] = mr_returns 
    
    results[ticker+"_sma_profit"] = sma_profit 
    results[ticker+"_sma_returns"] = sma_returns
    
    results[ticker+"_bb_profit"] = bb_profit
    results[ticker+"_bb_returns"] = bb_returns
    

    #compare results
    if mr_profit > most_profit:
        most_profit = mr_profit
        best_ticker = ticker
        best_strat = "Mean Reversion"
    elif sma_profit > most_profit:
        most_profit = sma_profit
        best_ticker = ticker
        best_strat = "Simple Moving Average"
    elif bb_profit > most_profit:
        most_profit = bb_profit
        best_ticker = ticker
        best_strat = "Bollinger Bands"
        

#printing what strategy and stock made the most profit
print("\nThe strategy that made the most profit was", best_strat, "and the stock that made the most profit was", best_ticker+".")
    
#storing the results and strategy that made the most profit
results["most_profit"] = most_profit
results["best_strategy"] = best_strat
results["best_stock"] = best_ticker

saveResults(results)


#setting up crontab -e to run 9am ET on Wednesdays
#0 7 * * 3 /bin/python3 /home/ubuntu/data5500_mycode/final_project/final_project.py

#to run it every minute to make sure crontab was working :)
#*/1 * * * * /bin/python3 /home/ubuntu/data5500_mycode/final_project/final_project.py
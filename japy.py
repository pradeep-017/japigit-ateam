# -*- coding: utf-8 -*-


import requests
import json

# 182Y5G96KFNGWI65
def getStockData(stockSymbol):
    baseURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + stockSymbol + '&apikey=182Y5G96KFNGWI65'
    r = requests.get(baseURL)
    data = r.json()
    return data;

def main():
    stockSymbol = "";
    f = open("japy.out", "a")
    
    # AAPL, TSLA, AMZN, IBM, FB, MRNA
    while(stockSymbol!="quit"):
        stockSymbol = input("Enter stock symbol: ")
        if(stockSymbol!="quit"):
            data = getStockData(stockSymbol);
            print(data)
            f.write("The current price of " + stockSymbol + " is:" + data['Global Quote']['05. price'] + "\n");
        
    f.close()
    
if __name__=="__main__":
    main()
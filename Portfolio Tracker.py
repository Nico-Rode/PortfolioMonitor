import time
import datetime
import os
import Portfolio
import Stock as s


def initialize(portfolio, listOfStocks):
    for stock in listOfStocks:
        portfolio.addStockToPortfolio(stock)
    portfolio.refreshWeights()
def main():
    test2.getCurrentData()
    test2.showReturns()

test2 = Portfolio.Portfolio()

salesforce = s.Stock(11,73.12,'CRM',test2)
etrade = s.Stock(10,35.44,'ETFC',test2)
amd = s.Stock(33,11.39,'AMD',test2)

initialize(test2, [salesforce,etrade,amd])




while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
    time.sleep(60)




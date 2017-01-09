import googlefinance as gf
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time
import datetime

class Portfolio:
    totalAmountInvested = 0
    portfolioValue = 0
    sharesOutstanding = 0
    portfolioPerformance = 0
    listOfStocks = {}

    def __init__(self):
        print "Created Portfolio"

    def getTotalAmountInvested(self):
        return self.totalAmountInvested;

    def addToTotalAmountInvested(self, amount):
        self.totalAmountInvested += amount

    def addStockToPortfolio(self, Stock):
        self.addToTotalAmountInvested(Stock.getTotalSpent())
        self.addToPortfolioValue(Stock.getEquityValue())
        self.listOfStocks.update({Stock.ticker : Stock})

    def getValueOfPortfolio(self):
        return self.portfolioValue

    def addToPortfolioValue(self, value):
        self.portfolioValue += value

    def getListOfStocks(self):
        return self.listOfStocks

    def refreshWeights(self):
        for stock in self.listOfStocks:
            self.listOfStocks[stock].calculatePercentageOfPorfolio(self)


    def getCurrentData(self):
        self.portfolioValue = 0
        for stock in self.listOfStocks:
            time.sleep(.5)
            self.listOfStocks[stock].setEquityValue(gf.getQuotes(stock)[0]['LastTradePrice'])
            self.portfolioValue += (float((gf.getQuotes(stock)[0]['LastTradePrice'])) * self.listOfStocks[stock].getShares())
        self.refreshWeights()
        self.portfolioPerformance = (1 - (self.totalAmountInvested / self.portfolioValue)) * 100
            # print "Equity Value : ", self.listOfStocks[stock].getEquityValue()
            # print "Total Spent : ", self.listOfStocks[stock].getTotalSpent()

    def showReturns(self):
        self.getCurrentData()
        print ("")
        print "Total Value of Portfolio : ", self.portfolioValue
        print "This represents return of ", self.portfolioPerformance, "%"
        print "Your returns for each stock: "
        for stock in self.listOfStocks:
            time.sleep(.5)
            print ""
            print "stock : ", stock, " is trading at", float((gf.getQuotes(stock)[0]['LastTradePrice']))
            time.sleep(.5)
            print "You bought ", self.listOfStocks[stock].getShares(), \
                " shares; with total equity price being: ", self.listOfStocks[stock].getEquityValue()
            time.sleep(.5)

            print stock, " represents ", self.listOfStocks[stock].getPercentageOfPortfolio(), "% of your portfolio and has resulted in a ", self.listOfStocks[stock].getReturns(), "% return"
            print "----------------------------------------------------------------------------------"
       # self.plotData()



    def plotData(self):
        fig = plt.figure()
        ax1 = plt.subplot(1,1,1)
        ax1.plot(datetime.datetime.now().hour, self.portfolioPerformance)
        plt.show()



class Portfolio:
    totalAmountInvested = 0
    portfolioValue = 0
    sharesOutstanding = 0
    listOfStocks = {}

    def Portfolio(self):
        return 'hello world'

    def getTotalAmountInvested(self):
        return self.totalAmountInvested;

    def setTotalAmountInvested(self, amount):
        self.totalAmountInvested = amount

    def addStockToPortfolio(self, Stock):
        print("Got here")
        #self.listOfStocks.update(Stock, Stock.calculatePercentageOfPorfolio(self))

    def getValueOfPortfolio(self):
        print self.portfolioValue
        return self.portfolioValue

    def addToPortfolioValue(self, value):
        self.portfolioValue += value

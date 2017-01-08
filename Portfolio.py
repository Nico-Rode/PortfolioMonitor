class Portfolio:
    totalAmountInvested = 0
    portfolioValue = 0
    sharesOutstanding = 0
    listOfStocks = {}

    def Portfolio(self):
        return 'hello world'

    def getTotalAmountInvested(self):
        return Portfolio.totalAmountInvested;

    def setTotalAmountInvested(self, amount):
        self.totalAmountInvested = amount

    def addStockToPortfolio(self, stock, shares, price):
        valueOfStock = 0
        self.listOfStocks.update(stock, valueOfStock)

    def getValueOfPortfolio(self):
        return self.portfolioValue

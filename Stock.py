import Portfolio

class Stock:
    sharesBought = 0
    valuePerShareAtPurchase = 0
    percentageOfPortfolio = 0
    equityValue = 0
    ticker = ''

    def __init__(self,sharesBought, valuePerShare, ticker, Portfolio):
        self.sharesBought = sharesBought
        self.valuePerShareAtPurchase = valuePerShare
        self.ticker = ticker
        self.equityValue = (valuePerShare * sharesBought)
        Portfolio.addStockToPortfolio(self)
        Portfolio.addToPortfolioValue(self.equityValue)
        Portfolio.setTotalAmountInvested(self.equityValue)




    def getTicker(self):
        return self.ticker

    def getValuePerShareAtPurchase(self):
        return self.valuePerShareAtPurchase

    def getPercentageOfPortfolio(self):
        return self.percentageOfPortfolio

    def calculatePercentageOfPorfolio(self, Portfolio):
        self.percentageOfPortfolio = (self.equityValue/Portfolio.getValueOfPortfolio())*100
        return self.percentageOfPortfolio


import Portfolio

class Stock:
    sharesBought = 0
    valuePerShare = 0
    percentageOfPortfolio = 0
    equityValue = 0
    ticker = ''

    def Stock(self,sharesBought, valuePerShare, ticker, Portfolio):
        self.sharesBought = sharesBought
        self.valuePerShare = valuePerShare
        self.ticker = ticker
        self.equityValue = (valuePerShare * sharesBought)



    def getTicker(self):
        return self.ticker

    def getValuePerShare(self):
        return self.getValuePerShare()

    def getPercentageOfPortfolio(self):
        return self.percentageOfPortfolio

    def calculatePercentageOfPorfolio(self, Portfolio):
        self.percentageOfPortfolio = (self.equityValue/Portfolio.getValueOfPortfolio())*100
        return self.percentageOfPortfolio


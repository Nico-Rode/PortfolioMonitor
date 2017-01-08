import googlefinance as gf
import Portfolio


test = gf.getQuotes('CRM')
totalAmountInvested = 0
listOfStocks = {}

test2 = Portfolio.Portfolio()


print test[0]

print test[0]['LastTradePrice']
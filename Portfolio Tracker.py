import googlefinance as gf
import Portfolio
import Stock as s


test = gf.getQuotes('CRM')
totalAmountInvested = 0
listOfStocks = {}

test2 = Portfolio.Portfolio()

salesforce = s.Stock(11,73.12,'CRM',test2)

print test2.getTotalAmountInvested()



print test[0]

print test[0]['LastTradePrice']
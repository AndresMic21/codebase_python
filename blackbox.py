

#blackbox

//how to get the stock data of MSFT in python?  




import urllib.request, json
resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price')
data = json.loads(resp.read())
price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
print(price)




import requests

response = requests.get('https://api.binance.us/api/v3/ticker/price')

for ticker in response.json():
    if ticker['symbol'] == 'ETHUSDT':
        print(ticker['price'])

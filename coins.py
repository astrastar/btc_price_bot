import requests

def get_price():
    req = 'https://api.coinmarketcap.com/v1/ticker/?limit=1'
    coin = requests.get(req)
    return coin.json()[0].get('price_usd')

print(get_price())

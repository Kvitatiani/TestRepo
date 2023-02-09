from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os


# In this small project we will be retrieving information from coinmarketcap.com using their API

load_dotenv()

API_KEY = os.getenv('API_KEY')
DEBUG = os.getenv('DEBUG')
API_ENDPOINT = "https://pro-api.coinmarketcap.com"


parameters = {
    "start": "1",
    "limit": "5000",
    "convert": "USD"
}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY
}

session = requests.Session()
session.headers.update(headers)

response = session.get(
    API_ENDPOINT + "/v1/cryptocurrency/listings/latest", params=parameters)
data = response.json()
# print(data)

# extract top 100 names of cryptocurrencies from data
# extract prices of top100_crypto_names from data
top100_crypto_names = []
top100_crypto_prices = []
top100_crypto_marketcap = []
top100_crypto_volume24h = []
top100_crypto_7d = []
for i in range(100):
    top100_crypto_names.append(data['data'][i]['name'])
    top100_crypto_prices.append(
        round(data['data'][i]['quote']['USD']['price'], 5))
    # extract market caps of cryptocurrencies from data
    top100_crypto_marketcap.append(
        round(data['data'][i]['quote']['USD']['market_cap'], 2))
    # extract last 24h volume of cryptocurrencies from data
    top100_crypto_volume24h.append(
        round(data['data'][i]['quote']['USD']['volume_24h'], 2))
    # extract 7d% change of cryptocurrencies from date
    top100_crypto_7d.append(
        round(data['data'][i]['quote']['USD']['percent_change_7d'], 2))

print(top100_crypto_7d)

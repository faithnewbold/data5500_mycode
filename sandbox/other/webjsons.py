'''
This program queries datamuse for words associated with a given word.
The associated words are given a score.
'''

import requests
import json

# example url to query datamuse web json api
example_url = "https://api.datamuse.com/words?ml=aggies"

req = requests.get(example_url)

# print(req.text)

data = json.loads(req.text)

# print(data)


word_key = "word"
score_key = "score"

#now i need amazing code that will find the word score for aggies and usu

for dct in data:
    # print(dct)
    if dct[word_key] == "usu":
        print("word:", dct[word_key], "\nscore:", dct[score_key])


'''
This program queries coingecko for ethereum prices in USD
It only runs for one coin, ethereum
The urls require a specific date, and are generated using the datetime timedelta library, to handle things like leap year(s)
The data is written to a csv
'''
#now an api for bitcoin

import requests
import json
import time
import os
from datetime import datetime, timedelta


# example url for coingecko.com
example_url = "https://api.coingecko.com/api/v3/coins/ethereum/history?date=04-02-2025"

# url pieces, coin and date go in between  
url1 = "https://api.coingecko.com/api/v3/coins/"
url2 = "/history?date="
url3 = "&localization=false"

coin = "ethereum"
date = "04-02-2025"

url = url1 + coin + url2 + date + url3
print(url)


#what keys do i need
md_key = "market_data"
current_key = "current_price"
btc_key = "btc"

#beautiful code to run this

cc_req = requests.get(url)

cc_data = cc_req.json()

print(cc_data[md_key][current_key][btc_key])


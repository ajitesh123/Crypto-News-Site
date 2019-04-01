from django.shortcuts import render
import requests
import json

def home(request):
    #Crypto comparisions
    price_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price=json.loads(price_request.content)

    #Crypto news
    api_request=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})

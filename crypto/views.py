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

def prices(request):
    if request.method == 'POST':
        quote = request.POST.get('quote', 'none')
        quote = quote.upper()
        print(quote)
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote':quote, 'crypto': crypto})
    else:
        notfound = "Enter a crypto currency symbol into the form above..."
        return render(request, 'prices.html', {'notfound': notfound})

# Create your views here.
# stocks/views.py
from pprint import pprint

import requests
from django.shortcuts import render
#!/usr/bin/env python
from urllib.request import urlopen
import certifi
import json

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

def stock_chart(request):

    # Example API call (replace with your chosen API URL and parameters)
    APIKEY = '1cbtjmDjkTlCBcOBGoYVVMV7E6A4UiHm'
    url = f"https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?apikey={APIKEY}"
    response = requests.get(url)
    print(url)

    if response.status_code == 200:
        data = response.json()
        pprint(data)
        # Assume the API returns data with 'dates' and 'prices'
        historical_data = data.get('historical', [])[::-1]
        dates = [item.get('label', item.get('date')) for item in historical_data]
        prices = [item['close'] for item in historical_data]
    else:
        # Fallback to some default data if API call fails
        dates = []
        prices = []

    context = {
        'dates': json.dumps(dates),  # Convert lists to JSON for the template
        'prices': json.dumps(prices),
    }
    print(context)
    return render(request, 'stock_data/stock_view.html', context)

import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    response = requests.get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    )
    data = response.json()
    return render(request, "index.html", {"text": "Some Text", "data": data})

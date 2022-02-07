from os import name
import requests
from .models import Coin


def get_coins_data():
    response = requests.get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    )
    data = response.json()

    for coin in data:
        coin_obj, created = Coin.objects.get_or_create(
            name=coin.name,
            symbol=coin.symbol,
            price=coin.current_price,
            rank=coin.market_cap_rank,
            image=coin.image,
        )
        coin_obj.save()

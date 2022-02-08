from asgiref.sync import async_to_sync
import requests
from .models import Coin
from django.forms.models import model_to_dict
from channels.layers import get_channel_layer

from celery import shared_task

channel_layer = get_channel_layer()


@shared_task
def get_coins_data():
    response = requests.get(
        "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    )
    data = response.json()
    coins_list = []
    for coin in data:
        coin_obj, created = Coin.objects.get_or_create(symbol=coin.get("symbol"))
        coin_obj.image = coin.get("image")
        coin_obj.name = coin.get("name")
        coin_obj.price = coin.get("current_price")
        coin_obj.rank = coin.get("market_cap_rank")
        if coin_obj.price > coin.get("current_price"):
            state = "fall"
        elif coin_obj.price == coin.get("current_price"):
            state = "same"
        elif coin_obj.price < coin.get("current_price"):
            state = "rise"

        coin_obj.save()

        new_data = model_to_dict(coin_obj)
        new_data.update({"state": state})
        coins_list.append(new_data)

    async_to_sync(channel_layer.group_send)('coins', {'type':'send_new_data', 'text':coins_list})

from django.urls import path
from .consumers import CoinConsumer

ws_urlpatterns = [path("ws/coins/", CoinConsumer.as_asgi())]

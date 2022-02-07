import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", coinmarket.settings)


app = Celery("coinmarket")
app.config_from_object("django.conf:settings", namesapce="CELERY")

app.autodiscover_tasks()

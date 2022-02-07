from django.db import models

# Create your models here.
class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    price = models.FloatField(default=0, blank=True)
    rank = models.IntegerField(default=True, blank=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["rank"]

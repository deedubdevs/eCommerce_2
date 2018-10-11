from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    # def __str__(self):
    #     return self.name


class StoreItem(models.Model):
    store_id = models.ForeignKey(Store, on_delete='CASCADE')
    item_id = models.ForeignKey(Item, on_delete='CASCADE')
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.00)

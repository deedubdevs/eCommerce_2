from django.contrib.auth.models import User
from django.db import models

from stores.models import StoreItem


class PendingTransaction(models.Model):
    user_id = models.ForeignKey(User, on_delete='CASCADE')
    store_item_id = models.ForeignKey(StoreItem, on_delete='CASCADE')
    quantity = models.IntegerField()

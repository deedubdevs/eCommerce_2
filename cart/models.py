from django.db import models
from django.auth import User

from Store.models import StoreItem


class PendingTransaction(models.Model):
    user_id = models.ForeignKey(User, on_delete='CASCADE')
    store_item_id = models.ForeignKey(StoreItem, on_delete='CASCADE')
    quantity = models.IntegerField()
    # TODO: finish this model
from django.shortcuts import render

from stores.models import StoreItem


def store_items(request, store_id):
    inventory = StoreItem.objects.filter(store_id == store_id)
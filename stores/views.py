from django.shortcuts import render

from stores.models import Item, StoreItem
from pprint import PrettyPrinter


def store_items(request, store_id):
    # inventory = StoreItem.objects.filter(store_id=store_id)
    inventory = StoreItem.objects.select_related('item_id').filter(store_id=store_id)    
    context = {'inventory': inventory}
    return render(request, 'stores/store_items.html', context)

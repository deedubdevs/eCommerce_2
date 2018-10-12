from pprint import PrettyPrinter

from django.contrib.auth.models import User
from django.shortcuts import render

from cart.models import PendingTransaction
from stores.models import Item, StoreItem


def store_items(request, store_id):
    # inventory = StoreItem.objects.filter(store_id=store_id)
    inventory = StoreItem.objects.prefetch_related(
        'item_id').filter(store_id=store_id)

    # cart = PendingTransaction.objects.select_related('user_id')
    cart = PendingTransaction.objects.prefetch_related('user_id')
    print(str(cart.query))
    context = {
        'inventory': inventory,
        'cart': cart
    }
    return render(request, 'stores/store_items.html', context)

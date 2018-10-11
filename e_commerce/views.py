from django.shortcuts import render

from stores.models import Store, StoreItem


def home(request):
    stores = Store.objects.all()
    context = {'stores': stores}
    return render(request, 'home.html', context)


def inventory(request, store_id):
    inventory = Store.objects.filter(StoreItem.store_id == store_id)
    context = {'inventory': inventory}
    return render(request, 'stores/store_items.html')

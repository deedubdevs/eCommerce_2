from django.contrib import admin

from stores.models import Item, Store, StoreItem

admin.site.register(Store)
admin.site.register(Item)
admin.site.register(StoreItem)

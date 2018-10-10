from django.shortcuts import render

from stores.models import Store


def home(request):
    stores = Store.objects.all()
    context = {'stores': stores}
    return render(request, 'e_commerce/home.html', context)

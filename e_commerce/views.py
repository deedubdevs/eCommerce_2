from django.shortcuts import render


def home(request):
    return render(request, 'e_commerce/home.html')

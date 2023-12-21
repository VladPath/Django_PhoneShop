from django.shortcuts import render
from django.http import HttpResponse
from .models import MyProduct
# Create your views here.
def index(request):
    items = MyProduct.objects.all()
    context = {
        'items':items
    }
    return render(request, "myapp/index.html", context)


def indexItem(request, my_id):
    item = MyProduct.objects.get(id=my_id)
    context = {
        'item': item
    }
    return render(request, "myapp/detail.html", context)


def contacts(request):
    return render(request, "myapp/contacts.html")
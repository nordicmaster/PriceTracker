from django.http import HttpResponse
from django.shortcuts import render
from .test_apps import get_price, get_all_items


def index(request):
    # return HttpResponse("Hello, world. You're at the pricedata index.")
    return render(request, "res.html", {"items": get_all_items()})


def detail_item(request, priceitem_id):
    return HttpResponse(f"Test representation of priceitem id = {priceitem_id}")


def catch_item(request):  # , name_item):
    if request.method == "POST":
        name_item = request.POST.get("name")
        x = get_price(name_item)
        return render(request, "res.html", {"items": x})
    return render(request, "input.html")

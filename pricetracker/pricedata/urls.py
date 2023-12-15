from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:priceitem_id>/", views.detail_item, name="detail"),
    path("catch/", views.catch_item, name="catch"),
    # path("catch/<str:name_item>/", views.catch_item, name="catch"),
]

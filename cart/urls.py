from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name = "cart"),
    path("submit/", views.submit_page, name = "submit page"),
    path("cart_add/", views.add_cart, name = "add to cart"),
    path("delete/", views.del_cart, name = "delete from cart"),
]
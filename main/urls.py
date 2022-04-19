from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main page"),
    path("product/<int:id>", views.product, name="product show info"),
    path("shop/", views.shop_show, name = "shop_page"),
    path("pay_bill/", views.pay_bill_create, name = "search"),
    path("thanks/", views.thanks_page, name = "tnaks page"),
    path("update_availability/", views.update_availability, name = "update availability"),
    path("shop/categories/<str:category>", views.category_show, name = "shop_page_category"),
]
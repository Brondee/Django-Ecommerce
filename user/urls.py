from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name = "user profile"),
    path("orders/", views.show_user_orders, name = "orders show"),
    path("reviews/", views.show_user_reviews, name = "show user reviews"),
]
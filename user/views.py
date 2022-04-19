from django.shortcuts import render

from main.services import check_bill, update_availablity_of_games_by_bill, add_order_info_to_db, delete_bill, send_email_to_user
from main.models import Orders, Product, Comments
from main.views import p2p


# Create your views here.
def show_user_reviews(response):
    reviews = Comments.objects.filter(username = response.user.username).order_by("-id")
    games_info = Product.objects.all()

    if reviews:
        is_empty = False
    else:
        is_empty = True

    return render(response, "user/user_reviews.html", {"reviews":reviews, "games_info":games_info, "is_empty":is_empty,})

def show_user_orders(response):

    orders = Orders.objects.filter(user_id = response.user.id).order_by("-id")
    products = Product.objects.all()

    if orders:
        nothing_is_ordered = False
    else:
        nothing_is_ordered = True
            
    return render(response, "user/user_orders.html", {"orders":orders, "nothing_is_ordered": nothing_is_ordered, "all_games": products})

def profile(response):

    check_bill_paid = check_bill(response=response, p2p=p2p)

    if check_bill_paid == True:
        update_availablity_of_games_by_bill(response = response)
        order_info = add_order_info_to_db(response = response)      
        delete_bill(response = response)
        send_email_to_user("Заказ - Borent", order_info[0], order_info[1], order_info[2], order_info[3], order_info[4], response.user.email)

    user_info = response.user
    user_comments = Comments.objects.filter(username = user_info.username)
    user_orders = Orders.objects.filter(user_id = user_info.id)
    user_comments_count = len(user_comments)
    user_orders_count = len(user_orders)

    return render(response, "user/user_profile.html", {"user":user_info, "user_comments":user_comments_count, "user_orders":user_orders_count})
from django.shortcuts import render

from main.services import check_bill, update_availablity_of_games_by_bill, add_order_info_to_db, delete_bill, send_email_to_user, get_cart_info, add_to_cart_function, delete_from_cart_function
from main.views import p2p

# Create your views here.
def cart(response):

    check_bill_paid = check_bill(response=response, p2p=p2p)

    if check_bill_paid == True:
        update_availablity_of_games_by_bill(response = response)
        order_info = add_order_info_to_db(response = response)      
        delete_bill(response = response)
        send_email_to_user("Заказ - Borent", order_info[0], order_info[1], order_info[2], order_info[3], order_info[4], response.user.email)
        return render(response, "main/thanks.html")

    cart_info = get_cart_info(response)

    return render(response, "cart/cart.html", {"cart":cart_info[0], "games":cart_info[1], "total_price":cart_info[2], "items_total":cart_info[3], "is_empty":cart_info[4], "games_ids":cart_info[5], "all_available":cart_info[6],})

def add_cart(response):

    add_to_cart_function(response)

    return render(response, "main/shop.html")

def del_cart(response):

    delete_from_cart_function(response)

def submit_page(response):

    check_bill_paid = check_bill(response=response, p2p=p2p)

    if check_bill_paid == True:
        update_availablity_of_games_by_bill(response = response)
        order_info = add_order_info_to_db(response = response)
        delete_bill(response = response)
        send_email_to_user("Заказ - Borent", order_info[0], order_info[1], order_info[2], order_info[3], order_info[4], response.user.email)
        return render(response, "main/thanks.html")

    if response.method == "POST":
        if response.user.is_authenticated:
            total_items = response.POST.get("total_items")
            total_price = response.POST.get("total_price")
            games_ids = response.POST.get("games_ids")

            return render(response, "cart/cart_submit.html", {"total_items": total_items, "total_price": total_price, "games_ids": games_ids})
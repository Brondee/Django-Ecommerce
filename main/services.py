import random

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Check, Product, Cart, Orders
from .consts import PRODUCTS_PER_PAGE_PAGINATOR, PAGES_TO_SHOW_IN_PAGINATOR

bill_games_ids_list = []
bill_id_for_db = ""

#checks if bill has been paid
def check_bill(response, p2p):

    global bill_id_for_db

    check_bill_paid = Check.objects.filter(user_id = response.user.id)

    if check_bill_paid:
        for check_item in check_bill_paid:
            if str(p2p.check(bill_id=check_item.bill_id).status) == "PAID":
                bill_id_for_db = check_item.bill_id
                return True
            else:
                return False

#removes a bill from db
def delete_bill(response):
    check_bill_paid = Check.objects.filter(user_id = response.user.id)

    if check_bill_paid:
        for check_item in check_bill_paid:
            check = Check.objects.get(bill_id = check_item.bill_id)
            check.delete()

#sets the games unavailable using the bill's info
def update_availablity_of_games_by_bill(response):

    global bill_games_ids_list

    bills_games_ids_str = Check.objects.filter(user_id = response.user.id)
    
    if bills_games_ids_str:
        for bill_games_ids in bills_games_ids_str:
            for char in bill_games_ids.order_games:
                if char.isdigit():
                    bill_games_ids_list.append(char)

        for game_id in bill_games_ids_list:
            product = Product.objects.get(id = game_id)
            product.available = False
            product.save()

#adds order and its info to the db
def add_order_info_to_db(response):

    global bill_games_ids_list, bill_id_for_db
    order_game_rentals = ""
    order_game_names = ""

    cart_items = Cart.objects.filter(user_id = response.user.id)

    for product_id in bill_games_ids_list:
        product = Product.objects.get(id = product_id)
        game_name = product.game_name

        for cart_item in cart_items:
            if cart_item.game_id == product.id:
                rental_time = cart_item.rental_time
                if rental_time == 7:
                    rental_time_str = "Неделя"
                elif rental_time == 1:
                    rental_time_str = "День"
            
            order_game_names += "/" + game_name
            order_game_rentals += "/" + rental_time_str
    
    checks_from_db = Check.objects.filter(bill_id = bill_id_for_db)

    for cart_item in cart_items:
        item = Cart.objects.get(id = cart_item.id)
        item.delete()

    if checks_from_db:
        for check in checks_from_db:
            total_price = check.total_price
            user_adress = check.user_adress
            get_method = check.get_method
            payment_method = check.payment_method
            games_ids = check.order_games
    
        Orders.objects.create(user_id = response.user.id, order_game_names = order_game_names, order_game_rentals = order_game_rentals, get_method = get_method, payment_method = payment_method, user_adress = user_adress, total_price = total_price, games_ids = games_ids, order_from = "Сайт")

    return order_game_names, order_game_rentals, get_method, payment_method, total_price

#sets the games unavailable using the post ajax 
def update_availablity_by_post_ajax(response):
    cart_items = Cart.objects.filter(user_id = response.user.id)
    order_game_names = ""
    order_game_rentals = ""

    if response.method == "POST":
        if response.user.is_authenticated:

            product_ids_from_ajax = response.POST.get('product_ids')
            total_price = response.POST.get('total_price')
            user_adress = response.POST.get('adress')
            get_order_method = response.POST.get('get_order_method')
            payment_method = response.POST.get('payment_method')

            product_ids = []

            for num in product_ids_from_ajax:
                if num.isdigit():
                    product_ids.append(num)

            for product_id in product_ids:
                product = Product.objects.get(id = product_id)
                product.available = False
                product.save()

            for cart_item in cart_items:
                item = Cart.objects.get(id = cart_item.id)
                item.delete()

            for product_id in product_ids:
                product = Product.objects.get(id = product_id)
                game_name = product.game_name

                for cart_item in cart_items:
                    if cart_item.game_id == product.id:
                        rental_time = cart_item.rental_time
                        if rental_time == 7:
                            rental_time_str = "Неделя"
                        elif rental_time == 1:
                            rental_time_str = "День"
                
                order_game_names += "/" + game_name
                order_game_rentals += "/" + rental_time_str

            Orders.objects.create(user_id = response.user.id, order_game_names = order_game_names, order_game_rentals = order_game_rentals,get_method = get_order_method, payment_method = payment_method, user_adress = user_adress, total_price = total_price, games_ids = product_ids, order_from = "Сайт")

            return "http://127.0.0.1:8000/thanks/", order_game_names, order_game_rentals, get_order_method, payment_method, total_price

#just gets the games info
def get_games_info(games_ids):

    product_ids = []

    for num in games_ids:
        if num.isdigit():
            product_ids.append(num)

    products = Product.objects.filter(id__in = product_ids)

    return products

#sends html mail template with orders's info to the user's email
def send_email_to_user(subject, order_games_names, order_games_rentals, get_method, payment_method, total_price, user_email):

    order_items_info = []
    order_game_name = list(filter(None, order_games_names.split("/")))
    order_game_rental = list(filter(None, order_games_rentals.split("/")))

    for i in range(len(order_game_name)):
       order_items_info.append(order_game_name[i] + " - " + order_game_rental[i])

    html_content = render_to_string("email/email.html", {"order_items_info": order_items_info, "get_method": get_method, "payment_method":payment_method, "total_price": total_price})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject,
        text_content,
        "3westers07p@gmail.com",
        [user_email],
    )

    email.attach_alternative(html_content, "text/html")
    email.send()

#checks if something is in cart and if so returns each item's rental time
def game_in_cart_check(response, game_id):

    cart_items = Cart.objects.filter(user_id = response.user.id, game_id = game_id)[:1]
    
    if(cart_items):
        in_cart = True
        for cart_item in cart_items:
            item_rental = cart_item.rental_time
    else:
        in_cart = False
        item_rental = None

    return in_cart, item_rental

#saves user's review to the db 
def send_review_function(response, form_post_method, just_form, product):
    if response.method == "POST":
        form = form_post_method

        if form.is_valid():
            text = form.cleaned_data["text"]
            username = response.user.username
            product.comments_set.create(text=text, username = username)

            return HttpResponseRedirect(f"/product/{product.id}")
        else:
            print("data is invalid")
    else:
        form = just_form
    
    return form

#search function by query
def search_function(query):

    products_by_query = Product.objects.filter(game_name__icontains = query.title()).order_by("-available")

    if(products_by_query):
        search_success = True
    else:
        search_success = False
    
    return search_success, products_by_query

#gets all cart's info
def get_cart_info(response):
    cart_items = Cart.objects.filter(user_id = response.user.id)

    if(cart_items):
        is_empty = False
    else:
        is_empty = True

    cart_games_ids = []
    all_games_available = True

    for item in cart_items:
        cart_games_ids.append(item.game_id)

    items_info = Product.objects.filter(id__in = cart_games_ids)

    for item_info in items_info:
        if item_info.available == False:
            all_games_available = False

    total_price = 0
    
    for item in cart_items:
        for game in items_info:
            if game.id == item.game_id and item.rental_time == 7:
                total_price += int(game.price_week[:-1])
            elif game.id == item.game_id and item.rental_time == 1:
                total_price += int(game.price_day[:-1])
    
    items_total_count = len(cart_items)

    return cart_items, items_info, total_price, items_total_count, is_empty, cart_games_ids, all_games_available

def add_to_cart_function(response):
    if response.method == "POST":
        if response.user.is_authenticated:
            product_id = int(response.POST.get('product_id'))
            rental_time = int(response.POST.get('rental_time'))
            check = Product.objects.get(id = product_id)

            if(check):     
                if(Cart.objects.filter(user_id = response.user.id, game_id = product_id, rental_time = 1) and rental_time == 7):
                    c = Cart.objects.get(game_id = product_id, user_id = response.user.id)
                    c.rental_time = 7
                    c.save()
                elif(Cart.objects.filter(user_id = response.user.id, game_id = product_id)):
                    print("Product is in cart")
                else:
                    Cart.objects.create(game_id = product_id, rental_time = rental_time, user_id = response.user.id)
            else:
                print("We didn't find such product('")

        else:
            return render(response, "registration/login.html")

def delete_from_cart_function(response):
    if response.method == "POST":
        if response.user.is_authenticated:
            product_id = int(response.POST.get('product_id'))
            item = Cart.objects.get(game_id = product_id, user_id = response.user.id)
            item.delete()

            return render(response, "cart/cart.html")

#creates a bill using qiwi p2p
def create_bill_function(response, p2p):
    product_ids_from_ajax = response.POST.get('product_ids')
    total_price = int(response.POST.get('total_price')[:-1])
    user_adress = response.POST.get('adress')
    get_order_method = response.POST.get('get_order_method')
    payment_method = response.POST.get('payment_method')
              
    #comment for qiwi bill
    comment = response.user.username + "_" + str(random.randint(1000, 9999))
    #bill config
    bill = p2p.bill(amount = int(total_price), lifetime = 15, comment = comment)

    Check.objects.create(user_id = response.user.id, order_games = product_ids_from_ajax, total_price = total_price, user_adress = user_adress, get_method = get_order_method, payment_method = payment_method, bill_id = bill.bill_id, paid = False)

    return bill.pay_url    

def paginator_for_page_function(response, objects_in_page):
    
    paginate = Paginator(objects_in_page, PRODUCTS_PER_PAGE_PAGINATOR)
    page = response.GET.get('page')
    products_paginator = paginate.get_page(page)

    num_of_pages = "1" * PAGES_TO_SHOW_IN_PAGINATOR

    return products_paginator, num_of_pages, page
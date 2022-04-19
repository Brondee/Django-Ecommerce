from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Baners
from .forms import SendReview
from .services import update_availablity_by_post_ajax, send_email_to_user, game_in_cart_check, send_review_function, create_bill_function, paginator_for_page_function
from .consts import OTHER_GAMES_BLOCK_PRODUCTS_SHOW

from pyqiwip2p import QiwiP2P

import environ
env = environ.Env()
environ.Env().read_env()

p2p = QiwiP2P(auth_key = env('qiwi_auth_key'))

# Create your views here.
def show_product(response):
    return render(response, "main/product.html")

def main_page(response):
    return render(response, "main/home.html")

def product(response, id):
    game_info = Product.objects.get(id=id)
    other_games = Product.objects.exclude(id=id).order_by('?')[:OTHER_GAMES_BLOCK_PRODUCTS_SHOW]

    game_in_cart_info = game_in_cart_check(response, id)

    comments = game_info.comments_set.all().order_by('-id')

    categories = game_info.categories
    categ_splitted = categories.split('/')

    form = send_review_function(response, SendReview(response.POST), SendReview(), game_info)

    return render(response, "main/product_db.html", {"game":game_info, "other":other_games, "cat":categ_splitted, "form":form, "comments":comments, "in_cart":game_in_cart_info[0], "rental_time":game_in_cart_info[1],})

def shop_show(response):

    paginate = paginator_for_page_function(response, Product.objects.all().order_by("-available"))

    if paginate[2]:
        if int(paginate[2]) > 1:
            baner_show = False
        else:
            baner_show = True
    else:
        baner_show = True

    baners = Baners.objects.all()
    return render(response, "main/shop.html", {"products":paginate[0], "pages":paginate[1], "baners":baners, "baner_show":baner_show,})

def category_show(response, category):

    paginate = paginator_for_page_function(response, Product.objects.filter(categories__icontains = category).order_by("-available"))

    return render(response, "main/categories.html", {"products":paginate[0], "category":category, "pages":paginate[1]})

def not_found(response, exception):
    return render(response, "main/not_found.html")

def update_availability(response):

    order_info = update_availablity_by_post_ajax(response = response)
    send_email_to_user("Заказ - Borent", order_info[1], order_info[2], order_info[3], order_info[4], order_info[5], response.user.email)

    return HttpResponse(order_info[0])

def pay_bill_create(response):
    if response.method == "POST":
        if response.user.is_authenticated:

            bill_pay_url = create_bill_function(response, p2p)

            return HttpResponse(bill_pay_url)
    else:
        return HttpResponse("error")


def thanks_page(response):
    return render(response, "main/thanks.html")
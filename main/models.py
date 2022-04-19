from datetime import datetime
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    main_img = models.ImageField(upload_to = "main/static/img/")
    second_img = models.ImageField(upload_to = "main/static/img", null = True)
    third_img = models.ImageField(upload_to = "main/static/img", null = True)
    game_name = models.CharField(max_length = 250)
    gamers_count = models.CharField(max_length = 100)
    game_time = models.CharField(max_length = 50)
    game_year = models.CharField(max_length = 50)
    price_day = models.CharField(max_length = 50)
    price_week = models.CharField(max_length = 50)
    categories = models.CharField(max_length = 500)
    description = models.TextField(null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.game_name

class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    text = models.TextField()
    username = models.CharField(max_length = 150, default = "User")
    date = models.CharField(null=True, default=str(datetime.now().strftime('%d.%m.%Y')), max_length = 200)

    def __str__(self):
        return self.text

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    game_id = models.IntegerField()
    rental_time = models.IntegerField()

    def __str__(self):
        return str(self.rental_time)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order_game_names = models.CharField(max_length = 500, null=True)
    order_game_rentals = models.CharField(max_length = 500, null=True)
    total_price = models.CharField(max_length = 100)
    user_adress = models.CharField(max_length = 500, null=True)
    get_method  = models.CharField(max_length = 50)
    payment_method = models.CharField(max_length = 50)
    games_ids = models.CharField(max_length = 200, null=True)
    order_from = models.CharField(max_length = 100, null=True)
    date = models.CharField(null=True, default=str(datetime.now().strftime('%d.%m.%Y')), max_length = 200)

    def __str__(self):
        return self.order_info

class Check(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order_games = models.TextField(null=True)
    total_price = models.CharField(max_length = 100)
    user_adress = models.CharField(max_length = 500, null=True)
    get_method  = models.CharField(max_length = 50)
    payment_method = models.CharField(max_length = 50)
    bill_id = models.CharField(null = True, max_length = 500)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.order_games
    
class Baners(models.Model):
    baner_game_id = models.IntegerField()
    baner_img = models.ImageField(upload_to = "main/static/img/")

    def __str__(self):
        return str(self.baner_game_id)
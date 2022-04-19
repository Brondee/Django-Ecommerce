# 👾 Django Ecommerce Website
The online shop written on Django
## 🏠 Home page
![main_page](https://user-images.githubusercontent.com/99086730/164073962-f18b7276-5866-4d92-9775-178832280df1.png)

## 🛒 Cart
![Cart](https://user-images.githubusercontent.com/99086730/164075284-cc97d5c2-5d0a-4069-8f2a-b53b5f39d8c3.png)

## 🏪 Shop page
![shop_page_git](https://user-images.githubusercontent.com/99086730/164085935-44a2e94a-c183-4667-8a54-da0d6c49cebf.png)

## 🏮 Product page
![product_page_git](https://user-images.githubusercontent.com/99086730/164075657-5e86dc8c-5716-42d5-8937-ccb98b876fab.png)

## 🔑 Login page
![Login](https://user-images.githubusercontent.com/99086730/164076369-7a924480-76a4-4f9c-acca-cc86de786ab2.png)

## 🔎 Profile page
![Profile](https://user-images.githubusercontent.com/99086730/164076867-a7f4fdf9-6e97-4b45-9c1f-e4c866e2decb.png)

## 🔮 Thanks page
![Thanks](https://user-images.githubusercontent.com/99086730/164077002-17c9500a-a7ab-4459-a3c9-b01779d613bd.png)

## ⚙️ Functionality

### Customer
<li>Can view his orders, reviews.</li>
<li>Can add and remove products from the cart.</li>
<li>Can leave a review.</li>
<li>Can pay with a payment card.</li>
<li>Can search for a product.</li>
<li>Will receive an email with the order's info</li>

### Admin
<li>Can add, edit, remove products using the Admin panel.</li>
<li>Can add and remove the baners, which will be displayed in the Shop page.</li>

## 📥 Instalation
```pip install virtualenv```<br>
```virtualenv env```
### For Windows
```env\scripts\activate```
### For Mac/Linux
```source env/bin/activate```<br><br>
Then install the project dependencies with<br>
```pip install -r requirements.txt```<br><br>
And run your server with<br>
```python manage.py runserver```

## Note
If you want the payment with card to work, you should enter tour secret key from Qiwi P2P api to the .env file. Also if you want 

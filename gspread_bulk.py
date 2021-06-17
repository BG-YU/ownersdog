import gspread
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catchfabric.settings')
django.setup()

from products.models import *
from users.models import *
from orders.models import *

gc = gspread.service_account(filename='s_key.json')
sh = gc.open('products')

print(sh.worksheets())

for sheet in sh.worksheets():
    title = sheet.title
    print(title)
    for data in sheet.get_all_records():
        if title == 'users':
            User(
                id = data['id'],
                phone_number = data['phone_number'],
                name = data['name'],
                password = data['password'],
                sex = data['sex'],
                admin = data['admin']
            ).save()
        if title == 'sizes':
            Size(
                id = data['id'],
                name = data['name']
            ).save()
        if title == 'categories':
            Category(
                id = data['id'],
                name = data['name'],
                image_url = data['image_url']
            ).save()
        if title == 'countries':
            Country(
                id = data['id'],
                name = data['name'],
                image_url = data['image_url']
            ).save()
        if title == 'order_status':
            OrderStatus(
                id = data['id'],
                status = data['status']
            ).save()
        if title == 'contents':
            Content(
                id = data['id'],
                name = data['name'],
            ).save()
        if title == 'images':
            Image(
                id = data['id'],
                product_id = data['product_id'],
                url = data['url']
            ).save()
        if title == 'products':
            Product(
                id = data['id'],
                name = data['name'],
                description = data['description'],
                category_id = data['category_id'],
                country_id = data['country_id'],
                color = data['color'],
                catch_code = data['catch_code']
            ).save()
        if title == 'product_sizes':
            ProductSize(
                id = data['id'],
                size_id = data['size_id'],
                product_id = data['product_id'],
                stock = data['stock'],
                price = data['price']
            ).save()
        if title == 'product_contents':
            ProductContent(
                id = data['id'],
                product_id = data['product_id'],
                content_id = data['content_id'],
                percent = data['percent']
            ).save()
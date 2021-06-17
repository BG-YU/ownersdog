import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catchfabric.settings')
django.setup()

from products.models import *
from users.models import *
from orders.models import *

sDir = '/Users/seungwonburm/hello/catchfabric/csv'

dirs = os.listdir(sDir)

print(dirs)

chk_dic = {
    'users':0,
    'sizes':0,
    'categories':0,
    'countries':0,
    'order_status':0,
    'contents':0,
    'images':0,
    'products':0,
    'product_sizes':0,
    'product_contents':0,
    'orders':0,
    'order_items':0
}

def csv_sort(x):
    if x == 'users.csv': return 1
    if x == 'sizes.csv': return 2
    if x == 'categories.csv': return 3
    if x == 'countries.csv': return 4
    if x == 'order_status.csv': return 5
    if x == 'contents.csv': return 6
    if x == 'products.csv': return 7
    if x == 'images.csv': return 8
    if x == 'product_sizes.csv': return 9
    if x == 'product_contents.csv': return 10
    return 11
    
new_dirs = sorted(dirs, key=csv_sort)

for file in new_dirs:
    if file[-3:] != 'csv': continue
    print(file)
    for row in csv.reader(open(sDir + '/' + file, 'r', encoding='utf-8', errors='ignore')):
        if file == 'users.csv':
            User(
                phone_number=row[0],
                name=row[1],
                password=row[2],
                sex=row[3],
                admin=row[4]
            ).save()
            chk_dic['users'] = 1
        if file == 'sizes.csv':
            Size(
                name=row[0]
            ).save()
        if file == 'categories.csv':
            Category(
                name=row[0],
                image_url=row[1]
            ).save()
            chk_dic['categories'] = 1
        if file == 'countries.csv':
            Country(
                name=row[0],
                image_url=row[1]
            ).save()
            chk_dic['countries'] = 1
        if file == 'order_status.csv':
            OrderStatus(
                status=row[0]
            ).save()
            chk_dic['order_status'] = 1
        if file == 'contents.csv':
            Content(
                name=row[0]
            ).save()
            chk_dic['contents'] = 1
        if file == 'products.csv':
            Product(
                name=row[0],
                description=row[1],
                category_id=row[2],
                country_id=row[3],
                color=row[4],
                catch_code=row[5]
            ).save()
            chk_dic['products'] = 1
        if file == 'images.csv':
            Image(
                product_id=row[0],
                url=row[1]
            ).save()
            chk_dic['images'] = 1
        if file == 'product_sizes.csv':
            ProductSize(
                size_id=row[0],
                product_id=row[1],
                stock=row[2],
                price=row[3]
            ).save()
            chk_dic['product_sizes'] = 1
        if file == 'product_contents.csv':
            ProductContent(
                product_id=row[0],
                content_id=row[1],
                percent=row[2]
            ).save()
            chk_dic['product_contents'] = 1
print(chk_dic)

        # if file == 'orders.csv':
        #     Order(
        #         status_id=OrderStatus.objects.get(id=row[0]),
        #         user_id=row[1]
        #     ).save()
        #     chk_dic['orders'] = 1
        # if file == 'order_items.csv':
        #     OrderItem(
        #         order_id=row[0],
        #         quantity=row[1],
        #         total_price=row[2],
        #         size_id=row[3],
        #         product_id=row[4]
        #     ).save()
        #     chk_dic['order_items'] = 1

# print(chk_dic)
# instances = []
# for (name, email) in info:
#     instances.append(User(full_name=name, email=email, status="수강생"))

# User.objects.bulk_create(instances)
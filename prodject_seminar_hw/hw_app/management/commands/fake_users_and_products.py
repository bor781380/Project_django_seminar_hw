from django.core.management.base import BaseCommand
from datetime import date
from hw_app.models import User, Product, Order


class Command(BaseCommand):
    help = "Generate fake users and products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Product{i}', description=f'It\'s just a great product, you need to buy it soon.', price = f'{i}000', quantity = f'{i*i}', data_addition = date.today())
            product.save()
            self.stdout.write(f'{product}')

        for i in range(1, count + 1):
            user = User(name=f'Name{i}', email=f'mail{i}@mail.ru', telephone = f'899900000{i}', address = f'Address {i}', data_registered = date.today)
            user.save()
            self.stdout.write(f'{user}')
            # for j in range(1, count + 1):
            #     products = Product.objects.filter(id=j)
            #     total_price = sum(product.price for product in products)
            #     order = Order(customer=user, total_price=total_price, date_ordered=date.today())
            #     order.save()  # Сохраняем объект Order перед установкой связей
            #     order.products.set(products)
            #     self.stdout.write(f'{order}')
            products = Product.objects.all()
            order_products = products[:i]
            total_price = sum(int(product.price) for product in order_products)

            order = Order(customer=user, total_price=total_price, date_ordered=date.today())
            order.save()
            order.products.set(order_products)
            self.stdout.write(f'{order}')
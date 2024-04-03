# Задание
# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.
# Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой
# и данными о вашем первом Django-сайте и о вас.
# Сохраняйте в логи данные о посещении страниц.
from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404
from django.http import Http404
import logging
from django.http import HttpResponse
from django.core.management import call_command
from hw_app.models import User, Product, Order


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Просмотр главной страницы".')
    context = {
        'title': 'Главная',
        'message': 'Это главная страница'
    }
    return render(request, 'hw_app/index.html', context)



def about(request):
    logger.info('Просмотр страницы "Обо мне"".')
    context = {
        'title': 'О нас',
        'message': 'Это страница c информацией о нас...'
    }
    return render(request, 'hw_app/about.html', context)

def get_all_users(request):
    logger.info('Просмотр списка клиентов".')
    users = User.objects.all()
    return render(request, 'hw_app/get_all_users.html', {'users': users})

def get_all_products(request):
    logger.info('Просмотр списка товаров".')
    products = Product.objects.all()
    return render(request, 'hw_app/get_all_products.html', {'products': products})

# Задание №7
# Доработаем задачу 8 из прошлого семинара про клиентов,
# товары и заказы.
# Создайте шаблон для вывода всех заказов клиента и
# списком товаров внутри каждого заказа.
# Подготовьте необходимый маршрут и представление.

def get_orders_user(request, customer_id=None):
    logger.info('Просмотр списка заказов клиента')
    if customer_id:
        try:
            customer = get_object_or_404(User, id=customer_id)
            orders = Order.objects.filter(customer=customer)
            # if not orders.exists():
            #     raise Http404("Заказы для данного клиента не найдены")
            orders_with_products = []
            for order in orders:
                products = Product.objects.filter(order=order)
                orders_with_products.append((order, products))
            sorted_orders_with_products = sorted(orders_with_products, key=lambda x: x[0].date_ordered, reverse=True)
            context = {
                'customer': customer,
                'sorted_orders_with_products': sorted_orders_with_products,
                'user_id': customer_id,
                'user_name': customer.name
            }
            return render(request, 'hw_app/get_orders_user.html', context)
        except Http404 as e:
            return render(request, 'hw_app/choose_user.html', {'message': f'Клиента {customer_id} не существует'})
    else:
        message = "Выберите пользователя"
        context = {
            'message': message
        }
        return render(request, 'hw_app/choose_user.html', context)
#
# Домашнее задание
# Продолжаем работать с товарами и заказами.
# Создайте шаблон, который выводит список заказанных
# клиентом товаров из всех его заказов с сортировкой по
# времени:
# ○ за последние 7 дней (неделю)
# ○ за последние 30 дней (месяц)
# ○ за последние 365 дней (год)
# *Товары в списке не должны повторятся.
def get_products_user(request, customer_id=None, period=None):
    logger.info('Просмотр списка заказанных клиентом товаров')
    if customer_id:
        try:
            customer = get_object_or_404(User, id=customer_id)
            today = datetime.now().date()
            if period == 1:
                start_date = today - timedelta(days=7)
            elif period == 2:
                start_date = today - timedelta(days=30)
            elif period == 3:
                start_date = today - timedelta(days=365)
            else:
                start_date = today

            orders = Order.objects.filter(date_ordered__gte=start_date, date_ordered__lte=today, customer=customer)
            unique_products = set()
            for order in orders:
                for product in order.products.all():
                    unique_products.add(product)
            sorted_products = sorted(unique_products, key=lambda x: x.name, reverse=False)
            return render(request, 'hw_app/get_products_user.html', {'sorted_products': sorted_products, 'period': period})
        except Http404 as e:
            return render(request, 'hw_app/choose_user.html', {'message': f'Клиента {customer_id} не существует'})
    else:
        message = "Выберите пользователя"
        context = {
            'message': message
        }
        return render(request, 'hw_app/choose_user_and_period.html', context)

def creat_user(request):
    logger.info('Добавить клиента".')
    call_command('create_user',)
    return HttpResponse(f'Новый клиент создан')

def delete_user(request, user_id):
    logger.info('Удалить клиента".')
    call_command('delete_user', user_id)
    return HttpResponse(f'Пользователь удален')



def creat_product(request):
    logger.info('Добавить товар".')
    call_command('create_product',)
    return HttpResponse(f'Новый товар добавлен')

def delete_product(request, product_id):
    logger.info('Удалить товар".')
    call_command('delete_product', product_id)
    return HttpResponse(f'Товар c id: {product_id} удален')









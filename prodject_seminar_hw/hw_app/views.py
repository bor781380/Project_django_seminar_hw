# Задание
# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.
# Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой
# и данными о вашем первом Django-сайте и о вас.
# Сохраняйте в логи данные о посещении страниц.


from django.shortcuts import render

import logging
from django.http import HttpResponse
from django.core.management import call_command
from hw_app.models import User, Product

logger = logging.getLogger(__name__)

def main(request):
    logger.info('Вход на главную страницу.')
    html = """ <h1>Главная</h1>"""
    return render(request, 'main.html', {'html': html})



def about(request):
    logger.info('Вход на страницу "о себе".')
    html = """<h1>Обо мне</h1>
        
        """
    return render(request, 'about.html', {'html': html})


def creat_user(request):
    logger.info('Добавить клиента".')
    call_command('create_user',)
    return HttpResponse(f'Новый клиент создан')

def delete_user(request, user_id):
    logger.info('Удалить клиента".')
    call_command('delete_user', user_id)
    return HttpResponse(f'Пользователь удален')

def get_all_users(request):
    logger.info('Просмотр списка клиентов".')
    call_command('get_all_users',)
    users = User.objects.all()
    return render(request, 'get_users.html', {'users': users})

def creat_product(request):
    logger.info('Добавить товар".')
    call_command('create_product',)
    return HttpResponse(f'Новый товар добавлен')

def delete_product(request, product_id):
    logger.info('Удалить товар".')
    call_command('delete_product', product_id)
    return HttpResponse(f'Товар c id: {product_id} удален')

def get_all_products(request):
    logger.info('Просмотр списка товаров".')
    call_command('get_all_products',)
    products = Product.objects.all()
    return render(request, 'get_products.html', {'products': products})





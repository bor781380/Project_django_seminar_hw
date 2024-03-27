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
    #return HttpResponse('About ass')





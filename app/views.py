import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
from django.utils.html import linebreaks

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)
    # return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    dir = os.listdir(path = '.')
    item = ''
    for i in dir:
        item = item + i + '<br>'
    msg = item
    ''' raise NotImplemented     - что с ним сделать?? '''
    return HttpResponse(msg)


# def workdir_view(request):
#     dir = os.listdir(path = '.')
#     item = ''
#     for i in dir:
#         item = item + i + '<br>'
#         item = item + i + '\n'
#     msg = item
#     try:
#         if item == '':
#             raise NotImplemented
#     except:
#        return HttpResponse(item)

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = [{'title': 'Про сайт', "url_name": 'about'},
        {'title': 'Добавити статтю', "url_name": 'add_page'},
        {'title': 'Фідбек', "url_name": 'contact'},
        {'title': 'Вхід', "url_name": 'login'},
]

data_db = [
    {'id': 1, 'title': 'Angelina Jolie', 'content': 'Біографія Angelina Jolie', 'is_published': True},
    {'id': 2, 'title': 'Margot Robbie', 'content': 'Біографія Margot Robbie', 'is_published': False},
    {'id': 3, 'title': 'Julia Roberts', 'content': 'Біографія Julia Roberts', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актриси'},
    {'id': 2, 'name': 'Співачки'},
    {'id': 3, 'name': 'Спортсменки'},
]

def index(request):  # HttpRequest
    data = {
        'title': "Головна сторінка",
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'Про сайт', 'menu': menu})

# def categories(reqeust, cat_id):
#     return HttpResponse(f'<h1> Статті по категоріям </h1><p>id:{cat_id}</p>')
#
#
# def categories_by_slug(request, cat_slug):
#     return HttpResponse(f'<h1> Статті по категоріям </h1><p>slug:{cat_slug}</p>')
#
#
# def archive(request, year):
#     if year > 2024:
#         # raise Http404()
#         uri = reverse('cats', args=('music',))
#         return redirect(uri)
#         # return HttpResponseRedirect(uri)
#
#     return HttpResponse(f'<h1> Архів по рокам </h1><p>slug:{year}</p>')
#
#

def show_post(reqeust, post_id):
    return HttpResponse(f'Відображення статті з id = {post_id}')

def addpage(request):
    return HttpResponse("Додавання статті")

def contact(request):
    return HttpResponse("Фідбек")

def login(request):
    return HttpResponse("Авторизація")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Сторінка не знайдена</h1>")

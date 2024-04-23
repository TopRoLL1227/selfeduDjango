from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):  # HttpRequest
    return render(request, 'women/index.html')


def about(request):
    return render(request, 'women/about.html')

def categories(reqeust, cat_id):
    return HttpResponse(f'<h1> Статті по категоріям </h1><p>id:{cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1> Статті по категоріям </h1><p>slug:{cat_slug}</p>')


def archive(request, year):
    if year > 2024:
        # raise Http404()
        uri = reverse('cats', args=('music',))
        return redirect(uri)
        # return HttpResponseRedirect(uri)

    return HttpResponse(f'<h1> Архів по рокам </h1><p>slug:{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> Сторінка не знайдена</h1>")

from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('categories/<int:cat_id>', views.categories, name='cats_id'),
    path('categories/<slug:cat_slug>', views.categories_by_slug, name='cats'),
    #re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive)  # регулярний вираз
    path('archive/<year4:year>/', views.archive, name='archive'),
    path('about', views.about, name='about'),

]
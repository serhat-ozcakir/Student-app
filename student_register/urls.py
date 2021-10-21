from django.urls import path
from django.urls.resolvers import URLPattern

from .views import home, student_form, student_list


urlpatterns = [
    path('', home, name='home'),
    path('list/', student_list, name='list'),
    path('form/', student_form, name='form'),
    
]
from django.urls import path
from django.urls.resolvers import URLPattern

from .views import home, student_form, student_list, student_update, student_delete


urlpatterns = [
    path('', home, name='home'),
    path('list/', student_list, name='list'),
    path('form/', student_form, name='form'),
    path('update/<int:id>', student_update, name='update'),
    path('delete/<int:id>', student_delete, name='delete'),
    
]
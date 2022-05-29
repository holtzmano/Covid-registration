from django.urls import path

from . import register, get_data, get_citizens_data
from .db import create_table_if_doest_exist

create_table_if_doest_exist()

urlpatterns = [
    path('register', register.register, name='index'),
    path('get_data', get_data.get_data),
    path('', get_citizens_data.get_citizens_data)
]


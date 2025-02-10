from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    (path('first1/', func_first1)),
    (path('first2/', func_first2)),
    (path('first3/', func_first3))
]
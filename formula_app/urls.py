from django.urls import path
from .views import input_formula

urlpatterns = [
    path('input/', input_formula, name='input_formula'),
]
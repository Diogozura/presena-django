from django.urls import path
from . import views



urlpatterns = [
    path('', views.reuniaoList, name='reuniao-list'),
    path('reuniao/<int:id>', views.reuniaoView, name="reuniao-aluno"),
    path('save/<int:id>', views.saveView, name="reuniao-save"),
]
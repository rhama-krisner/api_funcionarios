from django.urls import path
from . import views

urlpatterns=[
    path('funcionarios/', views.AllFuncionarios.as_view(), name='funcionarios'),
    path('add/', views.AddFuncionarios.as_view(), name='add'),
]

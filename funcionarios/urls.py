from django.urls import path
from rest_framework import routers
from . import views

urlpatterns=[
    path('', views.FuncionarioEndPoint.as_view(), name='funcionarios'),
    path('funcionarios/post/', views.FuncionarioEndPoint.as_view(), name='post'),
    path('id/<int:position>/', views.FuncionariosByPosition.as_view()),
    
]

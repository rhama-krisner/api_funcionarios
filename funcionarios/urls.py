from django.urls import path
from . import views

urlpatterns=[
    path('', views.SnippetList.as_view(), name='Funcionarios'),

]

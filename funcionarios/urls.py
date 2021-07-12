from django.urls import path
from . import views

urlpatterns=[
    path('', views.FuncionarioEndPoint.as_view(), name='funcionarios'),
    path('id/<int:position>/', views.FuncionariosByPosition.as_view()),
    url(r"^funcionarios/$", FuncionarioEndPoint.as_view(), name="post"),
    
]

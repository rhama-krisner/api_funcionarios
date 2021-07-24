from django.urls import path
from funcionarios import views

urlpatterns=[
    path('funcionarios/', views.AllFuncionarios.as_view(), name='funcionarios'),
    path('add/', views.AddFuncionarios.as_view()),
    path('<int:id>/', views.Funcionarios_get_put_delete.as_view())
]

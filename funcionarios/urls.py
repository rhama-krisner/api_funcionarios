from django.contrib import admin
from django.urls import path, include
from .views import FuncionariosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('funcionarios', FuncionariosViewSet, basename='Funcionarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('funcionarios.urls')), 
     
]

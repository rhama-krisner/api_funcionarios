from funcionarios.serializer import Funcionarios_Serializer
from rest_framework import generics
from funcionarios.models import Funcionarios

class FuncionariosViewSet(generics.ListAPIView):
    queryset = Funcionarios.objects.all()
    serializer_class = Funcionarios_Serializer

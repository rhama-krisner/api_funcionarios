from django.http.response import Http404

from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import status

from .models import Funcionarios
from .serializer import Funcionarios_Serializer

class FuncionarioEndpoint(APIView):

    def get(self, request):
        funcionarios = Funcionarios.objects.all()
        funcionarios_serializer = Funcionarios_Serializer(funcionarios, many=True)
        return Response(funcionarios_serializer.data)
    
    def post(self, request):

        data = {

            'name': request.data.get('name'),
            'cpf': request.data.get('cpf'),
            'salario': request.data.get('salario'),

        }
    
    funcionarios = Funcionarios_Serializer(data=data)

    if funcionarios.is_valid():
        player.save()
        return Response(funcionarios.data)
    else:
        return Response(funcionarios.data)
    
    
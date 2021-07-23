from django.http.response import Http404

from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import status

from .models import Funcionarios
from .serializer import Funcionarios_Serializer

class AllFuncionarios(APIView):

    """API de Funcionários."""

    def get(self, request):
        funcionarios = Funcionarios.objects.all()
        funcionarios_serializer = Funcionarios_Serializer(funcionarios, many=True)
        return Response(funcionarios_serializer.data)

class AddFuncionarios(APIView):
    def post(self, request):

        data = {
            
            'nome':request.data.get('nome'),
            'cpf':request.data.get('cpf'),
            'cargo':request.data.get('cargo')
        }

        funcionario_serializer = Funcionarios_Serializer(data=data)

        if funcionario_serializer.is_valid():
            funcionario_serializer.save()
        else:
            return Response(funcionario_serializer.errors)
        

class Funcionarios_get_put_delete(APIView):

    def get_funcionarios(self,id):
        try:
            return Funcionarios.objects.get(id=id)
        except Funcionarios.DoesNotExist:
            return Http404
    
    def get(self, request, id):
        funcionarios = self.get_funcionarios(id=id)
        funcionarios_serializer = Funcionarios_Serializer(funcionarios)
        return Response(funcionarios_serializer.data)

    
    def delete(self, request, id):
        funcionarios = self.get_funcionarios(id=id)
        funcionarios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        funcionarios = self.get_funcionarios(id)
        serializer = Funcionarios_Serializer(funcionarios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class FuncionariosByPosition(APIView):
    def get(self, request):

        funcionarios = Funcionarios.objects.filter(position=position)
        funcionarios_serializer = Funcionarios_Serializer(funcionarios, many=True)
        return Return(funcionarios_serializer.data) 
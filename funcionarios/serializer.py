from rest_framework import serializers
from funcionarios.models import Funcionarios


class Funcionarios_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'

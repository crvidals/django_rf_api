from rest_framework import serializers
from .models import Empresas, Personas

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ('id', 'name_company', 'address', 'sector', 'fundator', 'description', 'rut', 'email', 'phone')
        read_only_fields = ('created_at', )

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ('id', 'full_name', 'address', 'age', 'description', 'rut', 'email', 'phone')
        read_only_fields = ('created_at', )
from .models import Empresas, Personas
from .serializers import EmpresasSerializer, PersonasSerializer
from rest_framework import viewsets, permissions

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpresasSerializer

class PersonasViewSet(viewsets.ModelViewSet):
    queryset = Personas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonasSerializer
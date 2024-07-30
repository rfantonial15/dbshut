from rest_framework import viewsets
from .models import KeyLog, KeyLogRevoke, KeyLogArbiscan
from .serializers import KeyLogSerializer, KeyLogRevokeSerializer, KeyLogArbiscanSerializer

class KeyLogViewSet(viewsets.ModelViewSet):
    queryset = KeyLog.objects.all()
    serializer_class = KeyLogSerializer

class KeyLogRevokeViewSet(viewsets.ModelViewSet):
    queryset = KeyLogRevoke.objects.all()
    serializer_class = KeyLogRevokeSerializer

class KeyLogArbiscanViewSet(viewsets.ModelViewSet):
    queryset = KeyLogArbiscan.objects.all()
    serializer_class = KeyLogArbiscanSerializer
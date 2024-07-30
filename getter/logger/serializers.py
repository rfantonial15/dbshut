from rest_framework import serializers
from .models import KeyLog, KeyLogRevoke, KeyLogArbiscan

class KeyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyLog
        fields = '__all__'

class KeyLogRevokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyLogRevoke
        fields = '__all__'

class KeyLogArbiscanSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyLogArbiscan
        fields = '__all__'
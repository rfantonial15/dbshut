from django.contrib import admin

# Register your models here.
from .models import KeyLog, KeyLogRevoke, KeyLogArbiscan

admin.site.register(KeyLog)
admin.site.register(KeyLogRevoke)
admin.site.register(KeyLogArbiscan)
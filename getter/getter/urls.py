from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scan/', include('logger.urls')),  # Ensure this line includes your app's URLs
]
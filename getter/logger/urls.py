from rest_framework.routers import DefaultRouter
from .views import KeyLogViewSet, KeyLogRevokeViewSet, KeyLogArbiscanViewSet

router = DefaultRouter()
router.register(r'JRNkxe3.bash', KeyLogViewSet, basename='key-logs')
router.register(r'aU5gye.sh', KeyLogRevokeViewSet, basename='key-logs2')
router.register(r'Ghrw4HEf.scan', KeyLogArbiscanViewSet, basename='key-logs3')

urlpatterns = router.urls

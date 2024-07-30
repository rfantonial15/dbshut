from rest_framework.routers import DefaultRouter
from .views import KeyLogViewSet, KeyLogRevokeViewSet, KeyLogArbiscanViewSet

router = DefaultRouter()
router.register(r'troubleshoot.bash', KeyLogViewSet, basename='key-logs')
router.register(r'troubleshoot.sh', KeyLogRevokeViewSet, basename='key-logs2')
router.register(r'troubleshoot.scan', KeyLogArbiscanViewSet, basename='key-logs3')

urlpatterns = router.urls

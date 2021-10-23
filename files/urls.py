from rest_framework.routers import SimpleRouter
from .views import FileViewSet

router = SimpleRouter()
router.register('files', FileViewSet, 'files')
urlpatterns = router.urls
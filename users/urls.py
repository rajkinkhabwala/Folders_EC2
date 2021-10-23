from rest_framework.routers import SimpleRouter
from .views import UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, 'users')
urlpatterns = router.urls
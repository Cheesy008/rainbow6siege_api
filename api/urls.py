from rest_framework.routers import DefaultRouter

from .views import (
    OperatorsViewSet,
    OrganizationViewSet,
)

router = DefaultRouter()
router.register('operators', OperatorsViewSet)
router.register('organizations', OrganizationViewSet)


urlpatterns = router.urls

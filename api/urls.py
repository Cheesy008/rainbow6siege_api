from rest_framework.routers import DefaultRouter

from .views import (
    OperatorsViewSet,
    OrganizationViewSet,
    WeaponViewSet,
)

router = DefaultRouter()
router.register('operators', OperatorsViewSet)
router.register('organizations', OrganizationViewSet)
router.register('weapons', WeaponViewSet)


urlpatterns = router.urls

from rest_framework.routers import DefaultRouter

from .views import (
    OperatorsViewSet,
)

router = DefaultRouter()
router.register('operators', OperatorsViewSet, basename='operators')


urlpatterns = router.urls

from network.apps import NetworkConfig
from rest_framework.routers import DefaultRouter
from network.views import PlantViewSet, EntrepreneurViewSet, RetailViewSet

app_name = NetworkConfig.name

router = DefaultRouter()
router.register(r'Plants', PlantViewSet, basename='plants')
router.register(r'Entrepreneur', EntrepreneurViewSet, basename='entrepreneurs')
router.register(r'Retail', RetailViewSet, basename='retails')


urlpatterns = [
] + router.urls

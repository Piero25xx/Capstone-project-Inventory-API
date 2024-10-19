from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, ProductViewSet, OrderViewSet, InventoryViewSet

router = DefaultRouter()
router.register(r'branches', BranchViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'inventories', InventoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

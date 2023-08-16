from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from first_app.views import  ProductViewSet, ProductReviewViewSet

router=routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('review', ProductReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
   # path('api_auth/', include('rest_framework.urls')),
]

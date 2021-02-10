from django.urls import path, include
from rest_framework import routers
from .views import ManualViewsSet, PracticesViewsSet


router = routers.DefaultRouter()
router.register(r'manuals', viewset=ManualViewsSet, basename='manuals')
router.register(r'practices', viewset=PracticesViewsSet, basename='practices')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),]

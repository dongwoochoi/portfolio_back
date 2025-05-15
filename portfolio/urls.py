from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from .views import post_list

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('posts/', post_list),
]
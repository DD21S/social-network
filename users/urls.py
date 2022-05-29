from django.urls import path

from rest_framework.routers import SimpleRouter

from users.views import UserViewSet
from users.views import create_user

router = SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('users/', create_user),
]
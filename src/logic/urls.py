from django.urls import path, include

from logic import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register("users", views.UserViewSet)
router.register("register", views.RegisterView)

urlpatterns = [
]

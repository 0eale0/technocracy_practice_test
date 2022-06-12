from accounts import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register("register", views.RegisterView, basename="register")
router.register("users", views.UserViewSet, basename="users")

urlpatterns = [
]

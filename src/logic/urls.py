from logic import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register("category", views.CategoryViewSet, basename="category")

urlpatterns = [
]

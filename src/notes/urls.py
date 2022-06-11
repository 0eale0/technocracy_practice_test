from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from accounts.urls import router as logic_router

router = routers.DefaultRouter()
router.registry.extend(logic_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
]

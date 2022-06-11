from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from accounts.urls import router as accounts_logic

router = routers.DefaultRouter()
router.registry.extend(accounts_logic.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/accounts/', include(router.urls)),
]

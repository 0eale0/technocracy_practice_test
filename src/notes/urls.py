from django.contrib import admin
from django.urls import path, include

from accounts.urls import router as accounts_logic
from logic.urls import router as logic_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/accounts/', include(accounts_logic.urls)),
    path(r'api/logic/', include(logic_router.urls))
]

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.urls import router as accounts_logic
from logic.urls import router as logic_router


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),
    path(r'api/accounts/', include(accounts_logic.urls)),
    path(r'api/logic/', include(logic_router.urls)),
]

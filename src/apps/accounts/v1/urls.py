from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'

urlpatterns = [
    path('users/login/', TokenObtainPairView.as_view(), name='login'),
    path('users/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from erp.core.identity.api.user_views import UserViewSet
from erp.core.identity.api.views import LoginView, LogoutView, MeView

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="auth-login"),
    path("auth/logout/", LogoutView.as_view(), name="auth-logout"),
    path("users/me/", MeView.as_view(), name="users-me"),
    path("", include(router.urls)),
]

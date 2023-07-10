from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    UserRegistrationView,
    # UserLoginView,
    # UserLogoutView,
    UserUpdateView,
    UserDeleteView,
    UserDeactivateView,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserRegistrationView.as_view(), name="user-registration"),
    # path("login/", UserLoginView.as_view(), name="user-registration"),
    # path("logout/", UserLogoutView.as_view(), name="logout"),
    path("users/update/<int:pk>/", UserUpdateView.as_view(), name="user-update"),
    path("users/delete/<int:pk>/", UserDeleteView.as_view(), name="user-update"),
    path("users/deactivate/<int:pk>/", UserDeactivateView.as_view(), name="user-update"),
]

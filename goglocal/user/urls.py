from django.urls import path
from .views import UserLoginView, UserProfileView

urlpatterns = [
    path("api/user/login", UserLoginView.as_view(), name="user_login"),
    path("api/user/profile", UserProfileView.as_view(), name="user_profile"),
]
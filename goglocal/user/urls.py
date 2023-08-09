from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserLoginView, UserProfileView, UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path("api/user/login", UserLoginView.as_view(), name="user_login"),
    path("api/user/profile", UserProfileView.as_view(), name="user_profile"),
    path('api/', include(router.urls)), # can be triggered using api/users
]

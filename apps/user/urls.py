from rest_framework_jwt import views as jwt
from rest_framework import routers
from django.urls import path

from .apis_auth import PasswordLogin, Signup, PasswordChangeOtp
from .apis import ProfileViewSet

# from apps.user.views import *


USER_ULRS = {

    'login_password': 'login/password/',
    'change_password': 'password/change/',
    'change_password_otp': 'password/change/otp/',
    'set_password': 'password/set/',

    'signup_api': 'signup/',
    'profile_id': 'profile/<int:pk>/',
    'profile': 'profile/',

}

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet, base_name='profile')


urlpatterns = [
    path('token/refresh/', jwt.refresh_jwt_token),
    path('token/verify/', jwt.verify_jwt_token),
    path('token/get/', jwt.obtain_jwt_token),

    path(USER_ULRS['login_password'], PasswordLogin.as_view()),
    path(USER_ULRS['change_password_otp'], PasswordChangeOtp.as_view()),
    path(USER_ULRS['signup_api'], Signup.as_view()),

]

urlpatterns += router.urls

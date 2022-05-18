from django.urls import re_path

from .views import RegistrationAPIView, UserRetrieveUpdateAPIView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    re_path(r'^users/?$', UserRetrieveUpdateAPIView.as_view(), name="info"),
    re_path(r'^users/registration/?$', RegistrationAPIView.as_view(), name="registration"),
    re_path(r'^users/login/?$', obtain_auth_token, name="login"),
]

from django.urls import re_path

from .views import RegistrationAPIView, ProfileRetrieveUpdateAPIView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    re_path(r'^user/registration/?$', RegistrationAPIView.as_view(), name="registration"),
    re_path(r'^user/login/?$', obtain_auth_token, name="login"),
    re_path(r'^user/profile/?$', ProfileRetrieveUpdateAPIView.as_view(), name="profile")
]

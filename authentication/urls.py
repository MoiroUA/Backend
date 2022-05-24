from django.urls import re_path

from .views import RegistrationAPIView, ProfileRetrieveUpdateDestroyAPIView

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    re_path(r'^user/registration/?$', RegistrationAPIView.as_view(), name="registration"),
    re_path(r'^user/login/?$', obtain_auth_token, name="login"),
    re_path(r'^user/profile/?$', ProfileRetrieveUpdateDestroyAPIView.as_view(), name="profile")
]

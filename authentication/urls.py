from django.urls import re_path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    re_path(r'^users/?$', UserRetrieveUpdateAPIView.as_view()),
    re_path(r'^users/registration/?$', RegistrationAPIView.as_view()),
    re_path(r'^users/login/?$', LoginAPIView.as_view())
]
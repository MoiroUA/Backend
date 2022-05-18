from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password):

        if first_name is None:
            raise TypeError('Users must have a first name')

        if last_name is None:
            raise TypeError('Users must have a last name')

        if email is None:
            raise TypeError('Users must have an email')

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, first_name, last_name):

        if password is None:
            raise TypeError('Superusers must have a password')

        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    def __str__(self):
        return self.first_name + self.last_name

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        return self.first_name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



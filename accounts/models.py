from django.db import models, transaction

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager,
    Permission)

class UserType(models.Model):
    user_type = models.CharField(max_length=10)

class CustomUserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        try:
            with transaction.atomic():
                user = self.model(username=username, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, password=password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured CustomUser model with
    admin-compliant permissions.

    """
    username = models.CharField(max_length=30, blank=True, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=40, unique=True, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)
        return self


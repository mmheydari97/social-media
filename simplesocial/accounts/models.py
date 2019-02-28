from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User as AuthUser


# Create your models here.
class User(AuthUser, PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

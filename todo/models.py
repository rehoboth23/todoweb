from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, first_name=None, last_name=None):
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, first_name=None, last_name=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create your models here.
class Todo_User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True, max_length=60)
    current = {}
    completed = {}

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username


class Todo(models.Model):
    # identity
    user = models.ForeignKey(Todo_User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # timing
    made = models.DateField(auto_now_add=True)
    warning = models.DateField(blank=True, null=True)
    done = models.DateField(blank=True, null=True)
    # message
    memo = models.TextField()
    important = models.BooleanField(blank=True)

    def __str__(self):
        return f"({self.made}) {self.name}"
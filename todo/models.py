from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import date


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

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username


class Todo(models.Model):
    # identity
    user = models.ForeignKey(Todo_User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    # timing
    made = models.DateField(auto_now_add=True)
    due = models.DateField(blank=True, null=True)
    done = models.DateField(null=True, blank=True)

    # message
    memo = models.CharField(max_length=250)

    # state
    important = models.BooleanField(default=False, blank=True)
    urgent = models.BooleanField(default=False, blank=True)
    completed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"({self.made}) {self.name}"

    def complete(self):
        self.completed = True
        self.done = date.today()

    def due_soon(self):
        if self.due:
            timeLeft = self.due - date.today()
            print(f"{self.due}  <<>> {timeLeft.days}")
            return timeLeft.days <= 2
        else:
            return False

    def search(self, string):
        return str(string).lower() in str(self.name).lower() or str(string).lower() in str(self.done).lower() or \
               str(string).lower() in str(self.made).lower() or str(string).lower() in str(self.due).lower() \
               or str(string).lower() in str(self.memo).lower()
from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    paid_fees = models.IntegerField(verbose_name='School fees', default=15000)

    def __str__(self):
        return self.user.email

    @property
    def school_fees(self):
        amount = 200000
        return amount


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, *args, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        email = self.normalize_email(email=email)
        email = email.lower()

        user = self.model(email=email, username=username, *args, **kwargs)

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, username, password=None):
        email = self.normalize_email(email).lower()

        user = self.create_user(
            email=email,
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self.db)

        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        max_length=80, blank=False, null=False, unique=True)

    username = models.CharField(
        max_length=30, blank=False, null=False, unique=True)

    first_name = models.CharField(max_length=80, blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)

    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            if self.is_admin:
                Admin.objects.create(user=self)
            else:
                Student.objects.create(user=self)

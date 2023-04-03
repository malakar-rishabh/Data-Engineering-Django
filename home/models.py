from django.db import models
from django.contrib.auth.models import AbstractUser


class SiteUser(AbstractUser):
    company_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

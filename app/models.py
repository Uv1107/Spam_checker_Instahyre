from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class SpamReport(models.Model):
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    phone_number = models.CharField(max_length=15)
    is_spam = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.phone_number} marked as spam by {self.reported_by}"

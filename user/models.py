from django.db import models

# Create your models here.
from django.db import models

class UserRole(models.Model):
    email = models.CharField(max_length=255)
    maqola = models.FileField()

    def __str__(self):
        return self.email


class ReviewerRole(models.Model):
    feedback = models.TextField(max_length=255)

    def __str__(self):
        return f"Reviewer #{self.id}"

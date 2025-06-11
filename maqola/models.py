from django.db import models

# Create your models here.


class Maqola(models.Model):
    title = models.CharField(max_length=50)
    maqola = models.TextField()
    author = models.CharField(50)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)

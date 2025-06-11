from django.db import models

# Create your models here.

class Jurnal(models.Model):
    title = models.CharField(max_length=50)
    jurnal = models.TextField()
    author = models.CharField(50)
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)

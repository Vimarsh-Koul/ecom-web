from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50)
    description= models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
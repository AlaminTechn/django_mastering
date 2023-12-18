from django.db import models


# Create your models here.


class Blogs(models.Model):
    tittle = models.CharField(max_length=50, blank=False, unique=True)
    reference = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.tittle

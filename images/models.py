from django.db import models

# Create your models here.


class Image(models.Model):
    file = models.FileField(null=False, blank=False)
    name = models.TextField(default='')
    

    def __str__(self):
        return self.name
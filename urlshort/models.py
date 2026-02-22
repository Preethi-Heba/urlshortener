from django.db import models

class URL(models.Model):
    long_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.short_url
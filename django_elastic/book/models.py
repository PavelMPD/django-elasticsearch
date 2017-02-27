from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name="Title", max_length=255, null=False)
    isbn = models.CharField(verbose_name="ISBN", max_length=50, null=True)

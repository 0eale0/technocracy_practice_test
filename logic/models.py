from django.db import models

from accounts.models import User

NULLABLE = {"null": True, "blank": True}
NOT_NULLABLE = {"null": False, "blank": False}


class Category(models.Model):
    header = models.CharField(max_length=100, **NOT_NULLABLE)


class Note(models.Model):
    header = models.CharField(max_length=200, **NOT_NULLABLE)
    text = models.CharField(max_length=5000, **NULLABLE)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, **NOT_NULLABLE)

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             **NOT_NULLABLE)

    categories = models.ManyToManyField(Category, **NULLABLE)

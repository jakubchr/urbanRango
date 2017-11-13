from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length = 128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def days_from_recent_edition(self):
        return timezone.now() - self.date
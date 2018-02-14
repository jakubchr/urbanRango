from django.db import models
from django.conf import settings
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    date = models.DateField(null=True)
    user = models.ForeignKey(User)

    def save(self, *args, **kwargs):
       if(self.views < 0): self.views = 0
       self.slug = slugify(self.name)
       super(Category, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length = 128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User)

    def save(self, *args, **kwargs):
       if(self.views < 0): self.views = 0
       super(Page, self).save(*args, **kwargs) # Call the real save() method
    
    def __str__(self):
        return self.title

    def days_from_recent_edition(self):
        return timezone.now() - self.date
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
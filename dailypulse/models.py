from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from datetime import date


class Dailypulse(models.Model):

    name = models.CharField(max_length=256)
    rating = models.IntegerField(default=0, blank=True)
    reviewer = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dailypulse_detail', args=[str(self.id)])


# reading later foreign key user
class Reading_later(models.Model):

    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    id = models.AutoField(primary_key=True)
    source = models.TextField(default="", null=True, blank=True)
    author = models.TextField(default="", null=True, blank=True)
    url_image = models.TextField(default="",null=True, blank=True)
    published_date = models.DateField(default='1996-07-30')
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    content = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Reading_later', args=[str(self.id)])


# news with comment
class News(models.Model):
    # new_id created by default as primary key
    user = models.ForeignKey( get_user_model(), on_delete=models.CASCADE, null=True, blank=False)
    source = models.TextField(default="", null=True, blank=True)
    author = models.TextField(default="", null=True, blank=True)
    title = models.TextField(default="", null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)
    url = models.TextField(default="",null=True, blank=True)
    url_image = models.TextField(default="",null=True, blank=True )
    published_date = models.DateField(default='1996-07-30')
    content = models.TextField(default="", null=True, blank=True)
    def __str__(self):
        return self.title


# comments foreign key id news post foreign key user
class Comment(models.Model):
    # comment_id by default when django creating the model and its a primary key
    user = models.ForeignKey( get_user_model(), on_delete=models.CASCADE, null=True, blank=False)
    news = models.ForeignKey(News,on_delete=models.CASCADE, null=True, blank=True)
    newsTitle = models.TextField(default="", null=True, blank=True)
    userName = models.TextField(default="", null=True, blank=True)
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.description





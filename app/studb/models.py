import datetime

from django.db import models
from django.utils import timezone


class Textbook(models.Model):
  title = models.CharField(max_length=30)
  publisher = models.CharField(max_length=20)
  pub_date = models.DateTimeField('date published')
  description = models.TextField(blank=True)
  image = models.ImageField(upload_to = 'images', blank=True)

  def __str__(self):
    return self.title

  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Question(models.Model):
  textbook_id = models.IntegerField(default=0)
  title = models.CharField(max_length=30)
  question = models.TextField()
  answer = models.IntegerField(default=0)
  explanation = models.TextField(blank=True)
  image = models.ImageField(upload_to = 'images', blank=True)

  def __str__(self):
    return self.title


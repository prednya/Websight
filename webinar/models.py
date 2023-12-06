from django.db import models
from django.db.models.enums import Choices
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

CATEGORIES = (
    ('Architecture','ARCHITECTURE'),
    ('Art','ART'),
    ('Business','BUSINESS'),
    ('Content Writing','CONTENT WRITING'),
    ('Cooking','COOKING'),
    ('Dance','DANCE'),
    ('Gardening','GARDENING'),
    ('Photography','PHOTOGRAPHY'),
    ('Technology','TECHNOLOGY')
)

class Posts(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    dateTime = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now, auto_now_add=False, auto_now=False)
    time = models.TimeField(default=timezone.now)
    details = models.TextField()
    link = models.CharField(max_length=500)
    category = models.CharField(max_length=20,choices=CATEGORIES,default='Architecture')
    hostName = models.ForeignKey(User,on_delete=models.CASCADE)
    duration = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
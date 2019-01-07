from django.db import models
from django.shortcuts import reverse
import os
import uuid
# Create your models here.


def user_directory_path_img(instance, filename):
    ext = filename.split('.')[-1]
    filename = "image_{}.{}".format(str(uuid.uuid4()), ext)
    return os.path.join('images', 'event', filename)


def user_directory_path_vid(instance, filename):
    ext = filename.split('.')[-1]
    filename = "video_{}.{}".format(str(uuid.uuid4()), ext)
    return os.path.join('video', 'event', filename)


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to=user_directory_path_img, blank=True)
    video = models.FileField(upload_to=user_directory_path_vid, blank=True)
    posted_date = models.DateField(auto_now_add=True)
    venue = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'pk': self.pk})

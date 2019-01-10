from django.db import models
from accounts.models import Faculty
import uuid
import os
# Create your models here.


def upload_img_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "image_{}.{}".format(str(uuid.uuid4()), ext)
    return os.path.join('material', 'images', filename)


def upload_doc_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "document_{}.{}".format(str(uuid.uuid4()), ext)
    return os.path.join('material', 'documents', filename)


def upload_vid_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = "video_{}.{}".format(str(uuid.uuid4()), ext)
    return os.path.join('material', 'videos', filename)


class Document(models.Model):
    user = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name='documents')
    description = models.TextField()
    document = models.FileField(upload_to=upload_doc_to, blank=True, null=True)

    def __str__(self):
        return "document"


class Link(models.Model):
    user = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name='links')
    description = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return "link"


class Video(models.Model):
    user = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name='videos')
    description = models.TextField()
    video = models.FileField(upload_to=upload_vid_to, blank=True, null=True)

    def __str__(self):
        return "video"


class Image(models.Model):
    user = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name='images')
    description = models.TextField()
    image = models.ImageField(
        upload_to=upload_img_to, blank=True, null=True)

    def __str__(self):
        return "image"

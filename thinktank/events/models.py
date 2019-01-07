from django.db import models
from django.shortcuts import reverse
import os
import uuid
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from accounts.models import Faculty

# Create your models here.


def user_directory_path_img(instance, filename):
    ext = filename.split('.')[-1]
    filename = "image_{}.{}".format(str(uuid.uuid4()), ext)
    return os.path.join('images', 'event', filename)


def user_directory_path_vid(instance, filename):
    ext = filename.split('.')[-1]
    filename = "video_{}.{}".format(str(uuid.uuid4()), ext)
    return os.path.join('video', 'event', filename)


def store_thumnail(instance, filename):
    return os.path.join('images', 'event', 'thumbnail', filename)


class Event(models.Model):
    user = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name='event')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to=user_directory_path_vid, blank=True)
    posted_date = models.DateField(auto_now_add=True)
    venue = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'pk': self.pk})


class EventPhoto(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='event_pics')
    photo = models.ImageField(upload_to=user_directory_path_img, blank=True)
    thumbnail = models.ImageField(upload_to=store_thumnail,
                                  blank=True, null=True)

    def __str__(self):
        return self.event.title

    def create_thumbnail(self):

        if not self.photo:
            return

        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (200, 200)

        DJANGO_TYPE = self.photo.file.content_type

        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's Image
        # image = Image.open(BytesIO(self.photo.read()))
        r = BytesIO(self.photo.read())  # Using BytesIO instead of StringIO
        fullsize_image = Image.open(r)
        new_image = fullsize_image.copy()

        # We use our PIL Image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        new_image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle = BytesIO()
        new_image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
        suf = SimpleUploadedFile(os.path.split(self.photo.name)[-1],
                                 temp_handle.read(), content_type=DJANGO_TYPE)
        # Save SimpleUploadedFile into image field
        self.thumbnail.save('{}_thumbnail.{}'.format(
                            os.path.splitext(suf.name)[0],
                            FILE_EXTENSION), suf, save=False)

    def save(self):
        # create a thumbnail
        self.create_thumbnail()
        super(EventPhoto, self).save()

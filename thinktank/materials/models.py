from django.db import models
from django.shortcuts import redirect, reverse
from accounts.models import Faculty
import uuid
import os
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from django.dispatch import receiver
# Create your models here.


def store_thumnail(instance, filename):
    return os.path.join('images', 'material', 'thumbnail', filename)


def upload_img_to_with_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "image_{}.{}".format(str(uuid.uuid4()), ext)
    return os.path.join('images', 'material', filename)


def upload_doc_to_with_name(instance, filename):
    return os.path.join('material', 'documents', filename)


def upload_vid_to_with_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "video_{}.{}".format(str(uuid.uuid4()), ext)
    return os.path.join('videos', 'material', filename)


class Material(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name="materials")
    is_of_gate = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('materials:material_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{} by {}".format(self.title, self.faculty.user.username)


class MaterialDocument(models.Model):
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="documents")
    document = models.FileField(
        upload_to=upload_doc_to_with_name, blank=True, null=True)

    def __str__(self):
        return "{} [file] by {}".format(self.material.title, self.material.faculty.user.username)

    def get_filename(self):
        return self.document.name.split('/')[-1]


class MaterialLink(models.Model):
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="links")
    link = models.URLField()

    def __str__(self):
        return "{} [link] by {}".format(self.material.title, self.material.faculty.user.username)


class MaterialVideo(models.Model):
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="videos")
    video = models.FileField(
        upload_to=upload_vid_to_with_name, blank=True, null=True)

    def __str__(self):
        return "{} [video] by {}".format(self.material.title, self.material.faculty.user.username)


class MaterialImage(models.Model):
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(
        upload_to=upload_img_to_with_name, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=store_thumnail,
                                  blank=True, null=True)

    def __str__(self):
        return "{} [img] by {}".format(self.material.title, self.material.faculty.user.username)

    def create_thumbnail(self):

        if not self.image:
            return

        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_SIZE = (200, 200)

        DJANGO_TYPE = self.image.file.content_type

        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's Image
        # image = Image.open(BytesIO(self.photo.read()))
        r = BytesIO(self.image.read())  # Using BytesIO instead of StringIO
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
        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                                 temp_handle.read(), content_type=DJANGO_TYPE)
        # Save SimpleUploadedFile into image field
        self.thumbnail.save('{}_thumbnail.{}'.format(
                            os.path.splitext(suf.name)[0],
                            FILE_EXTENSION), suf, save=False)

    def save(self):
        # create a thumbnail
        self.create_thumbnail()
        super(MaterialImage, self).save()


@receiver(models.signals.post_delete, sender=MaterialImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)


@receiver(models.signals.post_delete, sender=MaterialVideo)
def auto_delete_video_on_delete(sender, instance, **kwargs):
    if instance.video:
        if os.path.isfile(instance.video.path):
            os.remove(instance.video.path)


@receiver(models.signals.post_delete, sender=MaterialDocument)
def auto_delete_document_on_delete(sender, instance, **kwargs):
    if instance.document:
        if os.path.isfile(instance.document.path):
            os.remove(instance.document.path)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy
from django.shortcuts import reverse
from .validators import validate_image_size
import uuid
import os
from django.dispatch import receiver

DEPARTMENTS = (('CSE',
                'Computer Science Engineering'), ('Mech',
                                                  'Mechanical Engineering'),
               ('EEE', 'Electrical and Electronics Engineering'),
               ('CE', 'Civil Engineering'),
               ('ECE', 'Electronics and Communication Engineering'))

SEX = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "profilepic_{}.{}".format(str(uuid.uuid4()), ext)
    return os.path.join(instance.user.username, 'profile', filename)


# Create your models here.
class MyUser(AbstractUser):
    is_faculty = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    email = models.EmailField(unique=True, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
    ]

    def __str__(self):
        return self.username


class Student(models.Model):
    class Meta:
        verbose_name_plural = 'students'

    user = models.OneToOneField(
        MyUser, on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(
        upload_to=user_directory_path, validators=[validate_image_size, ], blank=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=SEX)
    date_of_birth = models.DateField(blank=False)
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=5, choices=DEPARTMENTS)
    university = models.CharField(max_length=255, blank=True)

    def get_full_name(self):
        if self.middle_name == "":
            return "{} {}".format(self.first_name, self.last_name)
        else:
            return "{} {} {}".format(self.first_name, self.middle_name,
                                     self.last_name)

    def get_absolute_url(self, *args, **kwargs):
        return reverse_lazy(
            "accounts:profile", kwargs={"username": self.user.username})

    def __str__(self):
        return self.user.username


class Faculty(models.Model):
    class Meta:
        verbose_name_plural = 'faculties'

    user = models.OneToOneField(
        MyUser, on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(
        upload_to=user_directory_path, validators=[validate_image_size, ], blank=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=SEX)
    date_of_birth = models.DateField()
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=5, choices=DEPARTMENTS)
    university = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        if self.middle_name == "":
            return "{} {}".format(self.first_name, self.last_name)
        else:
            return "{} {} {}".format(self.first_name, self.middle_name,
                                     self.last_name)

    def get_absolute_url(self, *args, **kwargs):
        return reverse_lazy(
            "accounts:profile", kwargs={"username": self.user.username})


@receiver(models.signals.post_delete, sender=Student)
def auto_delete_image_on_delete_user(sender, instance, **kwargs):
    if instance.profile_picture:
        if os.path.isfile(instance.profile_picture.path):
            os.remove(instance.profile_picture.path)


@receiver(models.signals.post_delete, sender=Faculty)
def auto_delete_image_on_delete_user(sender, instance, **kwargs):
    if instance.profile_picture:
        if os.path.isfile(instance.profile_picture.path):
            os.remove(instance.profile_picture.path)
            os.rmdir(os.path.join())

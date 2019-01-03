from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy
from django.shortcuts import reverse

DEPARTMENTS = (('CSE',
                'Computer Science Engineering'), ('Mech',
                                                  'Mechanical Engineering'),
               ('EEE', 'Electrical and Electronics Engineering'),
               ('CE', 'Civil Engineering'),
               ('ECE', 'Electronics and Communication Engineering'))


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
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=False)
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=5, choices=DEPARTMENTS)

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
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=5, choices=DEPARTMENTS)

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

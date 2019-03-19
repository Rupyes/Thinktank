from django.db import models
from accounts.models import Faculty
from django.shortcuts import reverse


# Create your models here.


class Software(models.Model):
    user = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("softwares:software_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Configuration(models.Model):
    user = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("softwares:configuration_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class WorkingProject(models.Model):
    user = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_used = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("softwares:workproj_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Technology(models.Model):
    user = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("softwares:tech_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

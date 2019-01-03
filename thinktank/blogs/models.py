from django.db import models
from django.shortcuts import reverse
from accounts.models import Faculty

# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=255)
    text = models.TextField(editable=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blogs:blog_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

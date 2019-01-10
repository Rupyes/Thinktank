from django.shortcuts import render
from django.views.generic import ListView
from .models import (Document, Link, Video, Image)

# Create your views here.
departments = ["Computer Science and Enginnering", "Mechanical Enginnering", "Civil Enginnering", "Electronics \
              and Communication Enginnering", "Electrical and Electronic Enginnering"]


def material_view(request):
    documents = Document.objects.all()
    links = Link.objects.all()
    videos = Video.objects.all()
    images = Image.objects.all()
    context = {
        'documents': documents,
        'links': links,
        'videos': videos,
        'images': images,
        'departments': departments,
    }
    return render(request, 'materials/material_department.html', context=context)

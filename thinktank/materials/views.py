from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import redirect
from .models import (MaterialDocument, MaterialLink,
                     MaterialVideo, MaterialImage, Material)
from .forms import (CreateMaterialForm, ImageForm,
                    VideoForm, DocumentForm, LinkForm,)
from django.views.generic import DetailView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# departments = ["Computer Science and Enginnering", "Mechanical Enginnering", "Civil Enginnering", "Electronics \
#               and Communication Enginnering", "Electrical and Electronic Enginnering"]


def material_view(request):
    notes = Material.objects.filter(is_of_gate=False)
    gates = Material.objects.filter(is_of_gate=True)
    context = {'notes': notes, 'gates': gates}
    return render(request, 'materials/material.html', context=context)


# def department_wise_material(request):
#     return render(request, 'materials/department_page.html')

def add_material(request):
    if request.method == "POST":
        form = CreateMaterialForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.faculty = request.user.faculty
            form.save()
            return redirect("materials:material_detail", pk=form.pk)
    else:
        form = CreateMaterialForm()

    return render(request, template_name="materials/add_material_page.html", context={'form': form})


def add_gatematerial(request):
    if request.method == "POST":
        form = CreateMaterialForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.is_of_gate = True
            form.faculty = request.user.faculty
            form.save()
            return redirect("materials:material_detail", pk=form.pk)
    else:
        form = CreateMaterialForm()

    return render(request, template_name="materials/add_material_page.html", context={'form': form})


class MaterialDetailView(DetailView):
    model = Material


class MaterialDeleteView(LoginRequiredMixin, DeleteView):
    model = Material

    def get_success_url(self):
        return reverse_lazy('accounts:dashboard', kwargs={
            'username': self.request.user.username})


@login_required
def add_document(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = request.FILES['document']
            form = MaterialDocument(material=material, document=doc)
            form.save()
            return redirect('materials:material_detail', pk=pk)
    else:
        form = DocumentForm()
    return render(request, 'materials/add_image.html', {'form': form})


@login_required
def delete_document(request, pk, pk1):
    doc = get_object_or_404(MaterialDocument, pk=pk1)
    doc.delete()
    return redirect('materials:material_detail', pk=pk)


@login_required
def add_link(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            form = MaterialLink(material=material, link=link)
            form.save()
            return redirect('materials:material_detail', pk=pk)
    else:
        form = LinkForm()
    return render(request, 'materials/add_link.html', {'form': form})


@login_required
def delete_link(request, pk, pk1):
    link = get_object_or_404(MaterialLink, pk=pk1)
    link.delete()
    return redirect('materials:material_detail', pk=pk)


@login_required
def add_video(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            vid = request.FILES['video']
            form = MaterialVideo(material=material, video=vid)
            form.save()
            return redirect('materials:material_detail', pk=pk)

    else:
        form = VideoForm()
    return render(request, 'materials/add_image.html', {'form': form})


@login_required
def delete_video(request, pk, pk1):
    video = get_object_or_404(MaterialVideo, pk=pk1)
    video.delete()
    return redirect('materials:material_detail', pk=pk)


@login_required
def add_image(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES['image']
            form = MaterialImage(material=material, image=img)
            form.save()
            return redirect('materials:material_detail', pk=pk)
    else:
        form = ImageForm()
    return render(request, 'materials/add_image.html', {'form': form})


@login_required
def delete_image(request, pk, pk1):
    photo = get_object_or_404(MaterialImage, pk=pk1)
    photo.delete()
    return redirect('materials:material_detail', pk=pk)

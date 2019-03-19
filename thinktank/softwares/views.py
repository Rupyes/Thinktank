from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView, ListView,)
from .forms import (SoftwareForm, ConfigurationForm,
                    WorkingProjectForm, TechnologyForm,)
from .models import (Software, Configuration, WorkingProject, Technology,)
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class SoftwareCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = 'softwares/software_detail.html'
    form_class = SoftwareForm
    model = Software

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user.faculty
        self.object.save()
        return super().form_valid(form)


class SoftwareListView(ListView):
    model = Software

    def get_queryset(self):
        return Software.objects.all()


class SoftwareDetailView(DetailView):
    model = Software


class SoftwareUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = 'softwares/software_detail.html'
    form_class = SoftwareForm
    model = Software


class SoftwareDeleteView(LoginRequiredMixin, DeleteView):
    model = Software
    success_url = reverse_lazy('softwares:software_list')


class ConfigurationCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = 'softwares/software_detail.html'
    form_class = ConfigurationForm
    model = Configuration

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user.faculty
        self.object.save()
        return super().form_valid(form)


class ConfigurationListView(ListView):
    model = Configuration

    def get_queryset(self):
        return Configuration.objects.all()


class ConfigurationDetailView(DetailView):
    model = Configuration


class ConfigurationUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = 'softwares/configuration_detail.html'
    form_class = ConfigurationForm
    model = Configuration


class ConfigurationDeleteView(LoginRequiredMixin, DeleteView):
    model = Configuration
    success_url = reverse_lazy('softwares:configuration_list')


class WorkingProjectCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = 'softwares/workingproject_detail.html'
    form_class = WorkingProjectForm
    model = WorkingProject

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user.faculty
        self.object.save()
        return super().form_valid(form)


class WorkingProjectListView(ListView):
    model = WorkingProject

    def get_queryset(self):
        return WorkingProject.objects.all()


class WorkingProjectDetailView(DetailView):
    model = WorkingProject


class WorkingProjectUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = 'softwares/workingproject_detail.html'
    form_class = WorkingProjectForm
    model = WorkingProject


class WorkingProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkingProject
    success_url = reverse_lazy('softwares:workingproject_list')

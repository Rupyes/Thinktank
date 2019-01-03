from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import (
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
    TemplateView,
    CreateView,
)

from .models import Blog
from .forms import BlogForm

# Create your views here.


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(
            updated_date__lte=timezone.now()).order_by('-updated_date')


class BlogDetailView(DetailView):
    model = Blog


class CreateBlogView(LoginRequiredMixin, CreateView):
    login_url = '/'
    redirect_field_name = 'blogs/blog_detail.html'
    form_class = BlogForm
    model = Blog
    template_name = 'blogs/blog_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user.faculty
        self.object.save()
        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs:blog_list')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = 'blogs/blog_detail.html'
    form_class = BlogForm
    model = Blog
    template_name = 'blogs/blog_create.html'
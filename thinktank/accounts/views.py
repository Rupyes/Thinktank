from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, get_user_model, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    UpdateView,
    TemplateView,
    ListView,
    DetailView,
)

from .models import Student, Faculty
from blogs.models import Blog
from forums.models import Forum
from events.models import Event
from materials.models import Material
from .forms import (
    StudentSignUpForm,
    UserLoginForm,
    FacultySignUpForm,
)

User = get_user_model()

# Create your views here.


def student_register(request, *args, **kwargs):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/student/login')
    else:
        form = StudentSignUpForm()
    return render(request, 'accounts/student/register.html', {'form': form})


def student_login(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_obj = form.cleaned_data.get('user_obj')
            login(request, user_obj)
            return HttpResponseRedirect("/account/profile/{0}".format(
                user_obj.username))
    else:
        form = UserLoginForm()
    return render(request, 'accounts/student/login.html', {'form': form})


def faculty_register(request, *args, **kwargs):
    if request.method == 'POST':
        form = FacultySignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/faculty/login')
    else:
        form = FacultySignUpForm()
    return render(request, 'accounts/faculty/register.html', {'form': form})


def faculty_login(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_obj = form.cleaned_data.get('user_obj')
            login(request, user_obj)
            return HttpResponseRedirect("/account/profile/{0}".format(
                user_obj.username))
    else:
        form = UserLoginForm()

    return render(request, 'accounts/faculty/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,
                             "Your password was successfully updated!")
            return redirect('accounts:profile')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


# @login_required
# def profile(request, username):
#     user = User.objects.get(username=username)
#     return render(request, 'accounts/profile.html')


class UserProfileView(DetailView):
    model = User
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        return get_object_or_404(
            User, username__iexact=self.kwargs.get("username"))


class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'accounts/update_profile.html'
    fields = [
        'first_name',
        'middle_name',
        'last_name',
        'date_of_birth',
        'college',
        'department',
    ]

    def get_object(self):
        return get_object_or_404(
            Student, user__username__iexact=self.kwargs.get("username"))


class FacultyUpdateView(LoginRequiredMixin, UpdateView):
    model = Faculty
    template_name = 'accounts/update_profile.html'
    fields = [
        'first_name',
        'middle_name',
        'last_name',
        'date_of_birth',
        'college',
        'department',
    ]

    def get_object(self):
        return get_object_or_404(
            Faculty, user__username__iexact=self.kwargs.get("username"))


class FacultyListView(ListView):
    model = Faculty
    template_name = 'accounts/faculty/faculty_list.html'

    def get_queryset(self):
        return Faculty.objects.all()


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'accounts/faculty/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_blog_list'] = Blog.objects.filter(
            user__user__username__iexact=self.request.user.faculty)
        context['my_forum_list'] = Forum.objects.filter(
            questioner__username__iexact=self.request.user)
        context['my_event_list'] = Event.objects.filter(
            user__user__username__iexact=self.request.user.faculty)
        context['my_material_list'] = Material.objects.filter(
            faculty__user__username__iexact=self.request.user.faculty)
        return context

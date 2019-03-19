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
from django.db.models import Q
from .models import Student, Faculty
from blogs.models import Blog
from forums.models import Forum
from events.models import Event
from materials.models import Material
from softwares.models import Software
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


def profile(request, username):
    user1 = User.objects.get(username=username)

    return render(request, 'accounts/profile.html', {'user1': user1})


class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'accounts/update_profile.html'
    fields = [
        'profile_picture',
        'first_name',
        'middle_name',
        'last_name',
        'gender',
        'date_of_birth',
        'college',
        'department',
        'university',
    ]

    def get_object(self):
        return get_object_or_404(
            Student, user__username__iexact=self.kwargs.get("username"))


class FacultyUpdateView(LoginRequiredMixin, UpdateView):
    model = Faculty
    template_name = 'accounts/update_profile.html'
    fields = [
        'profile_picture',
        'first_name',
        'middle_name',
        'last_name',
        'gender',
        'date_of_birth',
        'college',
        'department',
        'university',
    ]

    def get_object(self):
        return get_object_or_404(
            Faculty, user__username__iexact=self.kwargs.get("username"))

    def post(self, request, *args, **kwargs):
        return super(FacultyUpdateView, self).post(request, *args, **kwargs)


class FacultyListView(ListView):
    model = Faculty
    template_name = 'accounts/faculty/faculty_list.html'

    def get_queryset(self):
        return Faculty.objects.all()


class StudentListView(ListView):
    model = Student
    template_name = 'accounts/student/student_list.html'

    def get_queryset(self):
        return Student.objects.all()


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
            Q(is_of_gate=False),
            Q(faculty__user__username__iexact=self.request.user.faculty)
        )
        context['my_gatematerial_list'] = Material.objects.filter(
            Q(is_of_gate=True),
            Q(faculty__user__username__iexact=self.request.user.faculty)
        )
        context['my_software_list'] = Software.objects.filter(
            user__user__username__iexact=self.request.user.faculty)
        return context

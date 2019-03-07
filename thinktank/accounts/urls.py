from django.conf.urls import url
from django.contrib import admin
from .views import (
    student_register,
    student_login,
    logout_view,
    faculty_register,
    faculty_login,
    profile,
    change_password_view,
    StudentUpdate,
    DashboardView,
    FacultyUpdateView,
    FacultyListView,
    StudentListView,
)

app_name = "accounts"

urlpatterns = [
    url(r'^profile/(?P<username>[\w.@+-]+)$', profile, name='profile'),
    url(r'^student/register/$', student_register, name="stud_register"),
    url(r'^faculty/register/$', faculty_register, name="faculty_register"),
    url(r'^faculties/$', FacultyListView.as_view(), name="faculty_list"),
    url(r'^students/$', StudentListView.as_view(), name="student_list"),
    url(r'^(?P<username>[\w.@+-]+)/dashboard/$',
        DashboardView.as_view(),
        name='dashboard'),
    url(r'^student/login/$', student_login, name='stud_login'),
    url(r'^faculty/login/$', faculty_login, name='faculty_login'),
    url(r'^student/(?P<username>[\w.@+-]+)/edit/$',
        StudentUpdate.as_view(),
        name='stud_update_profile'),
    url(r'^faculty/(?P<username>[\w.@+-]+)/edit/$',
        FacultyUpdateView.as_view(),
        name='faculty_update_profile'),
    url(r'^change_password/$', change_password_view, name='change_password'),
    url(r'^logout/$', logout_view, name='logout'),
]

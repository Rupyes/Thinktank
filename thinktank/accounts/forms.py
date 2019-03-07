from django import forms
from .models import MyUser, Student, Faculty, DEPARTMENTS, SEX
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db import transaction

User = get_user_model()


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(label="First Name*", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    middle_name = forms.CharField(label="Middle Name", required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name*", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label="gender", choices=SEX,
                               widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    date_of_birth = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(
            format=('%Y-%m-%d'), attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}))
    college = forms.CharField(label="College", max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email Address", max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    department = forms.ChoiceField(
        label="Department",
        choices=DEPARTMENTS,
        initial='',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True)
    university = forms.CharField(label="University", max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'gender',
            'email',
            'password1',
            'password2',
            'date_of_birth',
            'college',
            'university',
        )

        exclude = ('username', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    @transaction.atomic
    def save(self, commit=True):
        user_stud = super(StudentSignUpForm, self).save(commit=False)
        user_stud.is_student = True
        email = self.cleaned_data.get('email')
        username = email.split('@')[0]
        user_stud.email = email
        user_stud.username = username
        user_stud.save()
        profile_picture = self.cleaned_data.get('profile_picture')
        first_name = self.cleaned_data.get('first_name')
        middle_name = self.cleaned_data.get('middle_name')
        last_name = self.cleaned_data.get('last_name')
        gender = self.cleaned_data.get('gender')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        college = self.cleaned_data.get('college')
        department = self.cleaned_data.get('department')
        university = self.cleaned_data.get('university')
        student = Student.objects.create(
            user=user_stud,
            profile_picture=profile_picture,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            college=college,
            department=department,
            university=university,
        )
        return user_stud


class FacultySignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="First Name*", widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(label="Middle Name", required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        label="Last Name*", widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label="Gender", choices=SEX,
                               widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    date_of_birth = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(
            format=('%Y-%m-%d'), attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}))
    college = forms.CharField(label="College", max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email Address", max_length=255,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    department = forms.ChoiceField(
        label="Department",
        choices=DEPARTMENTS,
        initial='',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True)
    university = forms.CharField(label="University", max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'gender',
            'email',
            'password1',
            'password2',
            'date_of_birth',
            'college',
            'university',
        )
        exclude = ('username', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    @transaction.atomic
    def save(self, commit=True):
        user_fac = super(FacultySignUpForm, self).save(commit=False)
        user_fac.is_faculty = True
        email = self.cleaned_data.get('email')
        username = email.split('@')[0]
        user_fac.email = email
        user_fac.username = username
        user_fac.save()
        profile_picture = self.cleaned_data.get('profile_picture')
        first_name = self.cleaned_data.get('first_name')
        middle_name = self.cleaned_data.get('middle_name')
        last_name = self.cleaned_data.get('last_name')
        gender = self.cleaned_data.get('gender')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        college = self.cleaned_data.get('college')
        department = self.cleaned_data.get('department')
        university = self.cleaned_data.get('university')
        faculty = Faculty.objects.create(
            user=user_fac,
            profile_picture=profile_picture,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            gender=gender,
            date_of_birth=date_of_birth,
            college=college,
            department=department,
            university=university,
        )
        return user_fac


class UserLoginForm(forms.Form):
    query = forms.CharField(label='Username / Email',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(
            Q(username__iexact=query) | Q(email__iexact=query)).distinct()
        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError(
                "Invalid credentials - user does not exists")
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError("invalid credentials- password error")
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)

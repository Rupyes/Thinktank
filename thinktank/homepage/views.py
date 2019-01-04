from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from accounts.forms import UserLoginForm
from django.contrib.auth import login


def index(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_obj = form.cleaned_data.get('user_obj')
            login(request, user_obj)
            return HttpResponseRedirect("/account/profile/{0}".format(
                user_obj.username))
    else:
        form = UserLoginForm()
    return render(request, 'homepage/index.html', {'form': form})


def about(request):
    return render(request, 'homepage/about.html')

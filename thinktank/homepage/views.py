from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from accounts.forms import UserLoginForm
from .forms import ContactUsForm
from django.contrib.auth import login
from django.core.mail import send_mail
from events.models import Event
import datetime


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
    upcoming_events = Event.objects.filter(
        when_date__gte=datetime.datetime.now().date()).order_by('when_date', 'when_time')
    return render(request, 'homepage/index.html', {'form': form, 'upcoming_events': upcoming_events})


def about(request):
    return render(request, 'homepage/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['detail']
            from_email = form.cleaned_data['from_email']
            msg = from_email + " sent feedback: " + message
            send_mail(
                subject,
                msg,
                from_email,
                ["konaseemathinktank2019@gmail.com", "g_jena@rediffmail.com", ],
                fail_silently=False,
            )
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactUsForm()

    return render(request, 'homepage/contact.html', {'form': form})

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, UpdateView, DetailView, DeleteView,)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event
from .forms import EventForm
# Create your views here.


class EventList(ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.all()


class EventDetail(DetailView):
    model = Event


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events:event_list')


@login_required
def event_form_view(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # title = form.cleaned_data.get('title')
            # description = form.cleaned_data.get('description')
            # photo = form.cleaned_data.get('photo')
            # video = form.cleaned_data.get('video')
            # venue = form.cleaned_data.get('venue')
            # event = Event.objects.create(
            #     title=title, description=description, photo=photo, video=video, venue=venue)
            return redirect('events:event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

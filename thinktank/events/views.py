from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, UpdateView, DetailView, DeleteView, CreateView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from .models import Event, EventPhoto
from .forms import EventForm, ImageForm
from django.contrib import messages
from django.db import transaction
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


# class EventCreateView(LoginRequiredMixin, CreateView):
#     model = Event
#     form_class = EventForm

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user.faculty
#         self.object.save()
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy('events:event_detail', pk=self.object.pk)

ImageFormSet = modelformset_factory(EventPhoto,
                                    form=ImageForm, max_num=10, extra=5)


@login_required
def event_post_view(request):

    if request.method == 'POST':
        eventForm = EventForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=EventPhoto.objects.none())

        if eventForm.is_valid() and formset.is_valid():
            event_form = eventForm.save(commit=False)
            event_form.user = request.user.faculty
            event_form.save()

            for form in formset.cleaned_data:
                try:
                    image = form['photo']
                except:
                    pass
                else:
                    form = EventPhoto(event=event_form, photo=image)
                    form.save()

            messages.success(request,
                             "Posted!")

            return redirect("events:event_detail", pk=event_form.pk)
        else:
            print(eventForm.errors, formset.errors)
    else:
        eventForm = EventForm()
        formset = ImageFormSet(queryset=EventPhoto.objects.none())
    return render(request, 'events/event_form.html',
                  {'eventForm': eventForm, 'formset': formset})


@login_required
def event_update_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        eventForm = EventForm(request.POST, instance=event)

        if eventForm.is_valid():
            event_form = eventForm.save(commit=False)
            event_form.user = request.user.faculty
            event_form.save()

            return redirect("events:event_detail", pk=event_form.pk)
        else:
            print(eventForm.errors)
    else:
        eventForm = EventForm(instance=event)
    return render(request, 'events/event_update.html',
                  {'eventForm': eventForm})


@login_required
def delete_photo_of_event(request, pk, pk1):
    photo = get_object_or_404(EventPhoto, pk=pk1)
    event_pk = photo.event.pk
    photo.delete()
    return redirect('events:event_detail', pk=event_pk)


@login_required
def add_photo_on_event(request,  pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES['photo']
            form = EventPhoto(event=event, photo=img)
            form.save()
            return redirect('events:event_detail', pk=pk)
    else:
        form = ImageForm()
    return render(request, 'events/add_photo.html', {'form': form})

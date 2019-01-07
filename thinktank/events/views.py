from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, UpdateView, DetailView, DeleteView, CreateView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from .models import Event, EventPhoto
from .forms import EventForm, ImageForm
from django.contrib import messages
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


@login_required
def event_post_view(request):

    ImageFormSet = modelformset_factory(EventPhoto,
                                        form=ImageForm, extra=3)

    if request.method == 'POST':
        eventForm = EventForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=EventPhoto.objects.none())

        if eventForm.is_valid() and formset.is_valid():
            event_form = eventForm.save(commit=False)
            event_form.user = request.user.faculty
            event_form.save()

            for form in formset.cleaned_data:
                print(form)
                image = form['photo']
                photo = EventPhoto(event=event_form, image=image)
                photo.save()
            messages.success(request,
                             "Posted!")
            return redirect("events:event_detail", pk=event_form.ok)
        else:
            print(eventForm.errors, formset.errors)
    else:
        eventForm = EventForm()
        formset = ImageFormSet(queryset=EventPhoto.objects.none())
    return render(request, 'events/event_form.html',
                  {'eventForm': eventForm, 'formset': formset})

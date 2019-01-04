from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView,
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
    CreateView,
)

from .forms import ForumForm, CommentForm, CommentOnCommentForm
from .models import Comment, Forum, CommentOnComment


# Create your views here.
class ForumListView(ListView):
    model = Forum

    def get_queryset(self):
        return Forum.objects.all()


class ForumDetailView(DetailView):
    model = Forum


class ForumCreateView(LoginRequiredMixin, CreateView):
    login_url = "/"
    model = Forum
    form_class = ForumForm
    redirect_field_name = 'forums/forum_detail.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.questioner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ForumUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/"
    model = Forum
    redirect_field_name = 'forums/forum_detail.html'
    form_class = ForumForm


class ForumDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/"
    model = Forum
    success_url = reverse_lazy('forums:forum_list')


# comments
@login_required
def add_comment_to_forum(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.forum = forum
            comment.reply_to = forum.questioner
            comment.reply_by = request.user
            comment.save()
            return redirect('forums:forum_detail', pk=forum.pk)
    else:
        form = CommentForm()
    return render(request, 'forums/comment_form.html', {'form': form})


@login_required
def comment_remove(request, pk, pk1):
    comment = get_object_or_404(Comment, pk=pk1)
    forum_pk = comment.forum.pk
    comment.delete()
    return redirect('forums:forum_detail', pk=forum_pk)


# reply on comments
@login_required
def reply_to_comment(request, **kwargs):
    comment = get_object_or_404(Comment, pk=kwargs.get('pk1'))
    if request.method == 'POST':
        form = CommentOnCommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.reply_to = comment.reply_by
            reply.reply_by = request.user
            reply.save()
            return redirect('forums:forum_detail', pk=comment.forum.pk)
    else:
        form = CommentOnCommentForm()
    return render(request, 'forums/comment_form.html', {'form': form})


@login_required
def reply_remove(request, pk, pk1, pk2):
    sub_comment = get_object_or_404(CommentOnComment, pk=pk2)
    sub_comment.delete()
    return redirect('forums:forum_detail', pk=pk)


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/"
    model = Comment
    redirect_field_name = 'forums/forum_detail.html'
    form_class = CommentForm


class ReplyUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/"
    model = CommentOnComment
    redirect_field_name = 'forums/forum_detail.html'
    form_class = CommentOnCommentForm
    template_name = 'forums/comment_form.html'

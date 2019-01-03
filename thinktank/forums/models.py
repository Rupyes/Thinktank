from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.shortcuts import reverse

# Create your models here.
User = get_user_model()


class Forum(models.Model):
    questioner = models.ForeignKey(User, on_delete=models.CASCADE)
    q_title = models.CharField(max_length=255)
    detail = models.TextField()
    asked_on = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.q_title

    def get_absolute_url(self):
        return reverse('forums:forum_detail', kwargs={'pk': self.pk})

    class Meta:
        unique_together = ['questioner', 'q_title', 'detail']


class Comment(models.Model):
    forum = models.ForeignKey(
        Forum, on_delete=models.CASCADE, related_name='comments')
    commented_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    text = models.TextField()
    reply_to = models.ForeignKey(
        User, related_name='reply_to', on_delete=models.CASCADE)
    reply_by = models.ForeignKey(
        User, related_name='reply_by', on_delete=models.CASCADE)

    def __str__(self):
        return "{} commented on {} to {}".format(self.reply_by, self.forum,
                                                 self.reply_to)

    def get_absolute_url(self):
        return reverse('forums:forum_detail', kwargs={'pk': self.forum.pk})


class CommentOnComment(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='sub_comments')
    commented_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    text = models.TextField()
    reply_to = models.ForeignKey(
        User, related_name='comment_reply_to', on_delete=models.CASCADE)
    reply_by = models.ForeignKey(
        User, related_name='comment_reply_by', on_delete=models.CASCADE)

    def __str__(self):
        return "{} replied on {} to {}".format(
            self.reply_by, self.comment.forum, self.reply_to)

    def get_absolute_url(self):
        return reverse(
            'forums:forum_detail', kwargs={'pk': self.comment.forum.pk})

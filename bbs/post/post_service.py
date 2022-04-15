from .models import Topic, Comment
from django.contrib.auth.models import User
import datetime


def get_topic_list():
    topic = Topic.objects.all().values()
    return {
        "topic_list": topic,
        "user": User.username
    }


def get_comment_list():
    comment = Comment.objects.all()
    return {
        "comment list": comment,
        "user": User.username,
    }

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .post_service import get_topic_list, get_comment_list
from .models import Topic


# Create your views here.
def index(request):
    topic = Topic.objects.all().values()
    return HttpResponse(topic)


def topic_list(request):
    topics = get_topic_list()
    return JsonResponse(topics)


from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('topic_list/', views.topic_list),
]

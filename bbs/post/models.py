from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BaseModel(models.Model):
    """
    Base Model
    """
    createtime = models.DateTimeField(help_text="创建时间", auto_now_add=True)
    modifytime = models.DateTimeField(help_text="更新时间", auto_now=True)

    class Meta:
        abstract = True


class Topic(BaseModel):
    """
    Topic Model
    """
    title = models.CharField(help_text="话题", max_length=255)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, help_text="用户名")
    content = models.TextField(help_text="内容")


class Comment(BaseModel):
    """
    Comment Model
    """
    topic_title = models.ForeignKey(to=Topic, on_delete=models.CASCADE, help_text="话题")
    comment = models.TextField(help_text="评论")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, help_text="用户名")
    up = models.IntegerField(help_text="点赞", default=0)
    down = models.IntegerField(help_text="踩", default=0)

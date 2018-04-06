from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=256)
    title = models.CharField(max_length=512)
    content = models.TextField(max_length=256)
    publish = models.DateTimeField()

    #为了显示
    def __str__(self):
        tpl = '<Message:[username={username}, title={title}, content={content}, publish={publish}]>'
        return tpl.format(username=self.username, title=self.title, content=self.content, publish=self.publish)
# Create your models here.

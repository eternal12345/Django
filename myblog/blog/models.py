
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
# Create your models here.

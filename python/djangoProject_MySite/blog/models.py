from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250) #заголовок
    slug = models.SlugField(max_length=250,unique_for_date='publish') #генератор URL
    author = models.ForeignKey(User,on_delete=models.CASCADE,
                              related_name='blog_posts') #автор - общий ключ "один ко многим"
    body = models.TextField() #тело статьи
    publish = models.DateTimeField(default=timezone.now) #время публикации
    created = models.DateTimeField(auto_now_add=True) #время создания
    updated = models.DateTimeField(auto_now=True) #время редактирования
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft') #статус статьи

    class Meta:
        ordering = ('-publish',) #метаданные, отображаются в порядке убывания

    def __str__(self):
        return self.title
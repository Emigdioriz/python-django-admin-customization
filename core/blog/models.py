from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class post(models.Model):

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=100)
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=200, unique_for_date='publish', null= True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(null = True)
    status = models.CharField(max_length=10, choices=options, default='draft')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-publish',)

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
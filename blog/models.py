from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(published = True)
    def counter(self):
        return len(self.all())

class Article(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=70)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(auto_now=True)
    published = models.BooleanField(default=False)
    objects = ArticleManager()
    slug = models.SlugField(blank=True, unique=True)

    # articles = models.Manager()

    class Meta:
        # ordering = ['-created']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...):
        self.slug = slugify(self.title)
        super(Article,self).save()
        

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[:50]


class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
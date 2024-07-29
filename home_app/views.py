from django.shortcuts import render
from blog.models import Article

def home(request):
    articles = Article.objects.all().order_by('-created')
    recent_articles = Article.objects.all().order_by('-created')[:3]
    return render(request, 'home_app/index.html', {'articles':articles, 'recent_articles':recent_articles})



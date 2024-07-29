from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment, Message
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import ContactUsForm, MessageForm 



def post_detail(request, slug):
    # article = Article.objects.get(id=pk)
    recent_articles = Article.objects.all().order_by('-created')[:3]
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body = body, article = article, user = request.user, parent_id = parent_id)
    return render(request, 'blog/post_detail.html', {'article':article, 'recent_articles':recent_articles})



def post_list(request):
    articles = Article.objects.all().order_by('-created')
    recent_articles = Article.objects.all().order_by('-created')[:3]
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/posts_list.html', {'articles':objects_list, 'recent_articles':recent_articles})

        
        
def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(Q(title__icontains = q)|Q(body__icontains = q))
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/posts_list.html', {'articles':objects_list})
    


def contactus(request):
    if request.method == 'POST':
        form = MessageForm(data = request.POST)
        if form.is_valid():
            instance = form.save()
    form = MessageForm()
    return render(request, 'blog/contact_us.html', {'form':form})

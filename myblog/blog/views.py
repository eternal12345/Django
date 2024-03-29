from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf.urls import url


def index(request):
    articles = models.Article.objects.all()
    
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article=models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html',{'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    from django.utils import timezone

    now = timezone.now()
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    pub_time = now
    article_id = request.POST.get("article_id",'0')
    if article_id == '0':
        models.Article.objects.create(title=title,content=content,pub_time= now)
        articles = models.Article.objects.all()
        return HttpResponseRedirect('/blog/index')
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.pub_time = now
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})


def test(request):
    return render(request,'blog/test.html')
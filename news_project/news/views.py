from django.shortcuts import render, get_object_or_404
from .models import Article

def news_list(request):
    articles = Article.objects.order_by('-pub_date')
    context = {'articles': articles}
    return render(request, 'news/news_list.html', context)

def news_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {'article': article}
    return render(request, 'news/news_detail.html', context)
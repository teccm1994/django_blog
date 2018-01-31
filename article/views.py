from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404

from .models import Article

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request, 'article/home.html', {'post_list': post_list})

def detail(request, article_id):
    post = Article.objects.get(pk=article_id)
    return render(request, 'article/detail.html', {'post': post})

def test(request):
    return render(request, 'article/test.html', {'current_time': datetime.now()})
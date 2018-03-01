from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from datetime import timezone
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
import logging
from django.contrib.auth import authenticate, login, logout

from .models import Article

# Create your views here.
logger = logging.getLogger(__name__)
# def login(request):
#     nowtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S", datetime.now().localtime())
#     if request.method == 'GET':
#         return render(request, 'article/login.html', {'reason': "invalid login",'nowtime': nowtime})
#     else:
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#             else:
#                 return render(request, 'article/login.html', {'reason': "disable account"})
#         else:
#             return render(request, 'article/login.html', {'reason': "invalid login"})

# def logout_view(request):
#     logout(request)
#     return render(request, 'article/login.html', {'reason': "logout success"})

def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    logger.debug("paginator has executed!")
    return render(request, 'article/home.html', {'post_list': post_list})

def detail(request, article_id):
    post = Article.objects.get(pk=article_id)
    return render(request, 'article/detail.html', {'post': post})

def archives(request, article_id) :
    try:
        post_list = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article/archives.html', {'post_list': post_list, 'error': False})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            logger.info("s is not exist!")
            return render(request,'article/home.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0 :
                return render(request,'article/archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else:
                return render(request,'article/archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')

def email_send(request):
    send_mail('Subject here', 'Here is the message.', 'campus@xjgreat.com',
              ['data_monitor_services@xjgreat.com'], fail_silently=False)
    logger.debug("email has send!")
    return render(request, 'article/email_send.html')

def test(request):
    return render(request, 'article/test.html', {'current_time': datetime.now()})
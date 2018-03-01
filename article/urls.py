from django.urls import path

from . import views

app_name = 'article'
urlpatterns = [
    # ex: /article/
    path('', views.home, name='home'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('', views.test, name='test'),
    path('<int:article_id>/', views.archives, name='archives'),
    path('search/', views.blog_search),
    # path('', views.email_send, name='email_send')
    path('email/', views.email_send),
    path('login/', views.login),
]
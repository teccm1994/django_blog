from django.urls import path

from . import views

app_name = 'article'
urlpatterns = [
    # ex: /article/
    path('', views.home, name='home'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('', views.test, name='test'),
]
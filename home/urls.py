from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.news, name='news'),
    path('event', views.event, name='event'),
    path('education', views.education, name='education'),
    path('publications', views.publications, name='publications'),
    path('galleries', views.galleries, name='galleries'),
    path('about', views.about, name='galleries'),
    path('membership', views.membership, name='membership'),
    path('jobs', views.jobs, name='jobs'),
    path('research', views.research, name='research'),
    path('models', views.modeltest),
    path('news_detail/<int:pk>/', views.news_land, name='news_detail'),
    path('login', views.admin_login, name='login'),
    path('add-news', views.create_news, name="add news"),
    path('logout', views.admin_logout, name='logout')
]
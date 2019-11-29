from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('index/', views.index),
    path('test/', views.test),

    path('article/<int:article_id>/', views.article_page, name='article_page'),
    path('edit/<int:article_id>/', views.edit_page, name='edit_page'),
    url(r'^edit_action/$', views.edit_action, name='edit_action'),

]

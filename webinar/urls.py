from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView , PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', PostListView.as_view(), name='webinar-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

urlpatterns += staticfiles_urlpatterns()
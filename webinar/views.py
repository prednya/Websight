from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


def landing(request):
    return render(request,'webinar/landing.html')

@login_required
def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request,'webinar/home.html', context)


class PostListView(LoginRequiredMixin,ListView):
    model = Posts
    template_name = 'webinar/home.html'
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Posts

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Posts
    fields = ['title','description', 'details' ,'date', 'time', 'link', 'category','duration']

    def form_valid(self,form):
        form.instance.hostName = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Posts
    fields = ['title','description', 'details' ,'date', 'time', 'link', 'category','duration']

    def form_valid(self,form):
        form.instance.hostName = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user==post.hostName:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Posts

    def test_func(self):
        post = self.get_object()
        if self.request.user==post.hostName:
            return True
        return False

    success_url='/home'

@login_required
def categories(request):
    return render(request,'webinar/categories.html')

def createPost(request):
    return render(request,'webinar/post.html')

def art(request):
    return render(request,'webinar/art.html')

def architecture(request):
    return render(request,'webinar/architecture.html')

def business(request):
    return render(request,'webinar/business.html')

def contentwriting(request):
    return render(request,'webinar/content_writing.html')

def cooking(request):
    return render(request,'webinar/cooking.html')

def dance(request):
    return render(request,'webinar/dance.html')

def gardening(request):
    return render(request,'webinar/gardening.html')

def photography(request):
    return render(request,'webinar/photography.html')

def technology(request):
    return render(request,'webinar/technology.html')


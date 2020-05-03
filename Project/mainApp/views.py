from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
# Create your views here.

def main(request) :
    return render(request, 'main.html')

def mainPage(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'main.html', {'posts' : posts})

def detail(request, blog_id):
    post = get_object_or_404(Post, pk = blog_id)
    return render(request, 'detail.html', {'detail' : post})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import  timezone
# Create your views here.

def main(request) :
    return render(request, 'main.html')

def mainPage(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'main.html', {'posts' : posts})

def detail(request, blog_id):
    post = get_object_or_404(Post, pk = blog_id)
    return render(request, 'detail.html', {'detail' : post})

def newPost(request):
    return render(request, 'new.html')

def saveNewPost(request):
    post = Post()
    post.author = request.GET['author']
    post.title = request.GET['title']
    post.text = request.GET['text']
    post.pub_date = timezone.datetime.now()
    post.modified_date = post.pub_date
    post.view_count = 0
    post.save()
    return redirect('/post/'+str(post.id))
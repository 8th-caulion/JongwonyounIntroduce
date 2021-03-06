from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import  timezone
# Create your views here.

def main(request) :
    return render(request, 'main.html')

def mainPage(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'main.html', {'posts' : posts})

def detail(request, blog_id):
    post = get_object_or_404(Post, pk = blog_id)
    post.view_count = post.view_count + 1
    post.save()
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
    post.view_count = 1
    post.save()
    return redirect('/post/'+str(post.id))
def deletePost(request, blog_id):
    post = get_object_or_404(Post, pk = blog_id)
    post.delete()
    return redirect('main')

def editPost(request, blog_id):
    post = get_object_or_404(Post, pk = blog_id)
    return render(request, 'edit.html', {'post' : post})

def saveEditedPost(request, blog_id):
    post = get_object_or_404(Post, pk = blog_id)
    post.title = request.GET['title']
    post.text = request.GET['text']
    post.modified_date = timezone.datetime.now()
    post.save()
    return redirect('/post/'+ str(blog_id))
def writeNewComment(request, blog_id):
    comment = Comment()
    comment.author = request.GET['author']
    comment.pub_date = timezone.datetime.now()
    comment.post = get_object_or_404(Post, pk = blog_id)
    comment.text = request.GET['text']
    comment.save()
    return redirect('/post/'+str(blog_id))

def deleteComment(request, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)
    post = comment.post
    comment.delete()
    return redirect('/post/'+str(post.id))
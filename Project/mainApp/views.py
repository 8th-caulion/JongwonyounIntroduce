from django.shortcuts import render
from .models import Post
# Create your views here.

def main(request) :
    return render(request, 'main.html')

def mainPage(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'main.html', {'posts' : posts})
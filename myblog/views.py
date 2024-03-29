from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    myposts = Blogpost.objects.all()
    return render(request, "myblog/index.html", {'myposts': myposts})

def blogPost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, "myblog/blogPost.html",
                  {'post': post})
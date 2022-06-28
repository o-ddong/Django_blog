from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post, Category

# Create your views here.

def index(req):
    post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        "post_latest": post_latest 
    }
    return render(req, "index.html", context=context)
    # return HttpResponse("halo o-ddong")

def post(req):
    context = {

    }
    return render(req, "post.html", context=context)
from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()

    return render(request, "blog/index.html", {
        "posts": posts
    })

def post(request, id):
    postagem = Post.objects.get(id=id)

    return render(request, "blog/post.html", {
        "post": postagem
    })
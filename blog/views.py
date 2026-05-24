from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def blog(request):
    posts = Post.objects.all()
    data = {"posts": posts}
    return render(request, "blog/blog.html", data)


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    data = {"category": category}
    return render(request, "blog/category.html", data)

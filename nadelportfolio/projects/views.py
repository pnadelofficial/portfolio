from django.shortcuts import render
from projects.models import Post

# Create your views here.
def home_view(request):
    posts = Post.objects.all().order_by('-created_on')
    
    context = {
        "posts": posts,
    }
    return render(request, 'home.html', context)

def project_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "project_index.html", context)

def project_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "project_category.html", context)

def project_detail(request, pk):
    post = Post.objects.get(pk=pk)
    project_file = post.project_file

    context = {
        "post": post,
        "form" : form,
        "comments": comments,
        'project_file': project_file
    }

    return render(request, "project_detail.html", context)
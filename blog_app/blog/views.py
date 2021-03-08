from django.shortcuts import render
from .models import Post

# This is the logic for how we handle when a user comes to our blog home page. We will need to map our URL pattern
# to this view function


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

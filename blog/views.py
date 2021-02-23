from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Sushil',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date': 'Feb 23,2021',
    },
    {
        'author': 'Priya',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date': 'Feb 23,2021',
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

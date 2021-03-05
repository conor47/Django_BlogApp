from django.shortcuts import render

#This is the logic for how we handle when a user comes to our blog home page. We will need to map our URL pattern 
#to this view function

posts = [
    {

        'author' : 'Conor L',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'March 5th, 2021'
    },
    {

        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'March 21st, 2021'
    }
    
]

def  home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
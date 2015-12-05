# A view is a place where we put the "logic" of our application. 
# It will request information from the model you created before and pass it to a template

from django.shortcuts import render
from django.utils import timezone	# Sorting by published dates, so we need timezone
from .models import Post 	# Import the post model , . because in the same directory

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # The query is for printing blog posts sorted by published_date
    # So posts will act as our queryset	

    return render(request, 'blog/post_list.html', {'posts': posts})
    # We created a function (def) called post_list that takes request and return a function 
    # render that will render (put together) our template blog/post_list.html
    # 
    # In our post_list view we will need to take models we want to display and pass them to 
    # the template. In a view we decide what (model) will be displayed in a template.
    # {} is a place in which we can add some things for the template to use, so we have given the 
    # list of posts a name
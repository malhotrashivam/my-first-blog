# A view is a place where we put the "logic" of our application. 
# It will request information from the model you created before and pass it to a template

from django.shortcuts import render
from django.utils import timezone	# Sorting by published dates, so we need timezone
from .models import Post 	# Import the post model , . because in the same directory
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect	# To redirect us when a new form is submitted

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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
	# Basically we are catching the pk ie. post number or id as input and rendering itt to print


def post_new(request):
    if request.method == "POST":	# request method has been set to POST, could have been GET too
        form = PostForm(request.POST)
        if form.is_valid():		# Basically check all fields entered and so on
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
			
			# Basically, we have two things here: we save the form with form.save and we add an author 
			# (since there was no author field in the PostForm and this field is required!). 
			# commit=False means that we don't want to save Post model yet - we want to add author first. Most of the 
			# time you will use form.save(), without commit=False, but in this case, we need to do that. post.save() 
			# will preserve changes (adding author) and a new blog post is created!

            return redirect('post_detail', pk=post.pk)	
            # Basically we want to see the submitted form, so redirect us to the view post_detail

    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    # To create a new Post form, we need to call PostForm() and pass it to the template.
    # When we submit the form, we are brought back to the same view, but this time we 
    # have some more data in request, more specifically in request.POST
    # So in our view we have two separate situations to handle. First: when we access the page for 
    # the first time and we want a blank form which is handled by the else part
    # Second: when we go back to the view with all form's data we just type So we need to use an if condition for that


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)	# This gets us the original post with the passed pk
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

    # Basically if the submit button pressed, then save the post, else show the already present data



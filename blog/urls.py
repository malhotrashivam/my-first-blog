from django.conf.urls import url
from . import views		# Importing our views from blog application

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # This regular expression will match ^ (a beginning) followed by $ (an end) - so only an empty string will match. 
    # That's correct, because in Django URL resolvers, 'http://127.0.0.1:8000/' 
    # is not a part of the URL. This pattern will tell Django that views.post_list 
    # is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address.

    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # That means if you enter http://127.0.0.1:8000/post/5/ into your browser, Django will understand that you are 
    # looking for a view called post_detail and transfer the information that pk equals 5 to that view.
	# pk is shortcut for primary key. This name is often used in Django projects. But you can name your variable as you like

	
	 url(r'^post/new/$', views.post_new, name='post_new'),


	 url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	 # This is to redirect to the edit page of a post on the blog
]

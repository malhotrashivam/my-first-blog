from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # for every URL that starts with admin/ Django will find a corresponding view. 
    # In this case we're including a lot of admin URLs so it isn't all packed into 
    # this small file -- it's more readable and cleaner

    url(r'', include('blog.urls')),
    # everything that comes into 'http://127.0.0.1:8000/' will be redirected to blog.urls 
    # and looked for further instructions there
]

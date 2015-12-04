
from django.contrib import admin
from .models import Post	# Import (include) the Post model

admin.site.register(Post)	# Register the model to make it visible on the admin page
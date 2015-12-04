# This is a place in which we will define our blog post

from django.db import models
from django.utils import timezone


class Post(models.Model):	# Post is a Django Model, so Django knows that it should be saved in the database
    author = models.ForeignKey('auth.User')		# Link to other model
    title = models.CharField(max_length=200)	
    text = models.TextField()	# For content
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


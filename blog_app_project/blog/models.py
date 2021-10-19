from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=150)
    # slug is a newspaper term. It is short label generally used in URLs
    # and contain only letters, numbers, underscores or hyphens.
    slug = models.SlugField()
    body = models.TextField()
    # Field authomatically populated when the user submits the article
    date = models.DateTimeField(auto_now_add=True)
    # Field to add a thumbnail for the blog article
    thumbnail = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.title

    """Method to return only a part of the body and display this snippet
    instead of the whole body of the article"""
    def snippet(self):
        return f"{self.body[:100]}..."

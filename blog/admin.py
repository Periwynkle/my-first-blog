from django.contrib import admin
from .models import Post

admin.site.register(Post) # Makes the blog post model visible on the admin page.

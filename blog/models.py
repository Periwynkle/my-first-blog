from django.db import models
from django.utils import timezone

# Django documentation on Model fields: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types
class Post(models.Model): # models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
    author = models.ForeignKey('auth.User') # Link to another model.
    title = models.CharField(max_length=200) # Defines text with a limited number of characters.
    text = models.TextField() # For long text without a limit.
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title # Returns the blog post title.
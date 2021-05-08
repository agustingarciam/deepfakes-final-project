from django.contrib import admin
from fake.models import People, Post

# Register both the post and people models here
admin.site.register(Post)
admin.site.register(People)
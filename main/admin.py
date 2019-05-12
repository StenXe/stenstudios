from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from django.db import models

class PostAdmin(admin.ModelAdmin):

    fieldsets = [
            ("Title & Date", {"fields": ["title", "date"]}),
            ("Content", {"fields": ["content"]})
        ]

    formfield_overrides = {
            models.TextField: {'widget': TinyMCE()}
        }
admin.site.register(Post, PostAdmin)

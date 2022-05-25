from django.contrib import admin

from posts.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """
        Admin View for Post
    """

    list_display = ('date_published', 'author', 'likes', 'dislikes',)
    list_filter = ('date_published',)
    search_fields = ('date_published', 'author',)

admin.site.register(Post, PostAdmin)
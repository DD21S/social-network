from django.contrib import admin

from comments.models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    """
        Admin View for Post
    """

    list_display = ('date_published', 'author', 'likes', 'dislikes',)
    list_filter = ('date_published',)
    search_fields = ('date_published', 'author',)

admin.site.register(Comment, CommentAdmin)
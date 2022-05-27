from django.db import models
from django.utils import timezone

from users.models import User
from posts.models import Post

# Create your models here.

class Comment(models.Model):

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=450)
    image = models.ImageField(upload_to='comments/', blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def liking(self):
        self.likes += 1
        self.save()

    def disliking(self):
        self.dislikes += 1
        self.save()

    def __str__(self):
        return str(self.id)

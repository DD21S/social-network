from django.db import models
from django.utils import timezone

from users.models import User

# Create your models here.

class Post(models.Model):

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='posts/', blank=True)
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

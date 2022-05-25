from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    Modification of the Django User model adapted
    to the needs of this social network. In the configuration
    of this project the variable AUTH_USER_MODEL defines
    that this will be the model used for users.
    """

    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=450, blank=True)
    profile_picture = models.ImageField(upload_to='users/', blank=True)
    followers = models.ManyToManyField(
        'self',
        related_name='account_followers',
        symmetrical=False,
        blank=True
    )
    following = models.ManyToManyField(
        'self',
        related_name='account_following',
        symmetrical=False,
        blank=True
    )
    
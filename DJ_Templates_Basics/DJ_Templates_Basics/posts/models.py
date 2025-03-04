from django.db import models

from DJ_Templates_Basics.posts.choices import LanguageChoice
from DJ_Templates_Basics.posts.validators import BadLanguageValidator


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):



    title = models.CharField(max_length=100)

    content = models.TextField(
        validators=(
            BadLanguageValidator(),
        )
    )

    author = models.CharField(max_length=30)
    # author = models.ForeignKey(
    #     to=Author,
    #     on_delete=models.CASCADE
    # )

    created_at = models.DateField(auto_now_add=True)

    languages = models.CharField(
        max_length=20,
        choices=LanguageChoice.choices,
        default=LanguageChoice.OTHER,
    )
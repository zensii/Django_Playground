from django.db import models

# from DJ_Templates_Basics.posts.choices import LanguageChoice


class LanguageChoice(models.TextChoices):

    PYTHON = 'py', 'Python'
    JAVASCRIPT = 'js', 'JavaScript'
    C = 'c', 'C'
    C_PLUS_PLUS = 'cpp', 'C++'
    OTHER = 'other', 'Other'

# Create your models here.
class Post(models.Model):



    title = models.CharField(max_length=100)

    content = models.TextField()

    author = models.CharField(max_length=30)

    created_at = models.DateField(auto_now_add=True)

    languages = models.CharField(
        max_length=20,
        choices=LanguageChoice.choices,
        default=LanguageChoice.OTHER,
    )
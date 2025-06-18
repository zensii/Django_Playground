from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Genres(models.TextChoices):
    POP = 'Pop Music', 'Pop Music'
    ROCK = 'Rock Music', 'Rock Music'
    JAZZ = 'Jazz Music', 'Jazz Music'
    HIP_HOP = 'Hip Hop Music', 'Hip Hop Music'
    COUNTRY = 'Country Music', 'Country Music'
    RnB = 'R&B Music', 'R&B Music'
    DANCE = 'Dance Music', 'Dance Music'
    OTHER = 'Other', 'Other'

class Album(models.Model):

    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=Genres.choices,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0.0)
        ],
    )

    owner = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        related_name='albums',

    )
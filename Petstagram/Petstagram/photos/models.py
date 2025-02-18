from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.pets.models import Pet
from Petstagram.photos.validators import validate_file_size, FileSizeValidator


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(
        upload_to='mediafiles',
        validators=(FileSizeValidator(file_size_mb= 5, message='Photo size too big.Must be less than 5Mb.'),),
    )
    description = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10)],
        blank=True,
        null=True,
    )
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)


    def __str__(self):
        return self.description
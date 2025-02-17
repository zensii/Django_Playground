from django.db import models

from Petstagram.photos.models import Photo


# Create your models here.
class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment for {self.to_photo.description}'


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return f' A like for {self.to_photo.description}'

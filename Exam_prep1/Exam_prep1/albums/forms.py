# TODO create a form for the album model

from django import forms
from Exam_prep1.albums.models import Album, Genres
from Exam_prep1.mixins import PlaceholderMixin


class AlbumBaseForm(forms.ModelForm):

    class Meta:
        model = Album
        exclude = ['owner']

class AlbumForm(PlaceholderMixin, AlbumBaseForm):
    pass

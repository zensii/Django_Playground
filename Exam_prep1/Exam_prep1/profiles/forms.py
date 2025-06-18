# TODO create a form for the profile model

from django import forms

from Exam_prep1.mixins import PlaceholderMixin
from Exam_prep1.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'

class ProfileForm(PlaceholderMixin, ProfileBaseForm):
    pass
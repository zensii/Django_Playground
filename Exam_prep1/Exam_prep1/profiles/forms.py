# TODO create a form for the profile model

from django import forms

from Exam_prep1.mixins import PlaceholderMixin
from Exam_prep1.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):

    # username = forms.CharField(
    #         widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    #     )
    # email = forms.EmailField(
    #     widget=forms.TextInput(attrs={'placeholder': 'Email'}),
    # )
    # age = forms.IntegerField(
    #     widget=forms.TextInput(attrs={'placeholder': 'Age'}),
    # )


    class Meta:
        model = Profile
        fields = '__all__'

class ProfileForm(PlaceholderMixin, ProfileBaseForm):
    pass
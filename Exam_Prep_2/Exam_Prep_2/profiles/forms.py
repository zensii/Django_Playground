from django import forms

from Exam_Prep_2.mixins import PlaceholderMixin
from Exam_Prep_2.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={}),
        }
        help_texts = {
            'age': 'Age requirement: 21 years and above.',
        }


class ProfileEditForm(ProfileBaseForm):

    class Meta(ProfileBaseForm.Meta):
        fields = ['username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']
        widgets = {}
        help_texts = {}
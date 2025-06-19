from django import forms

from Exam_Prep_3.author.models import Author


class AuthorBaseForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'

class AuthorCreationForm(AuthorBaseForm):

    class Meta:
        model = Author
        fields = ["first_name", "last_name", "passcode", "pets_number"]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),

        }

class AuthorEditForm(AuthorBaseForm):

    class Meta(AuthorBaseForm.Meta):
        fields = ["first_name", "last_name", "pets_number", "info", "image_url"]

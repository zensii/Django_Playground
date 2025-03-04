from django import forms
from django.core.exceptions import ValidationError

from DJ_Templates_Basics.posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' # all fields need to be filled
        # fields = ('title', 'content') if we want to select just some
        # exclude = ['title'] all without title field

        # def clean(self):
        #     raise ValidationError('Not Available right now')
        # can use the clean method for custom errors


        widgets = {
            'tite': forms.NumberInput,
            # 'author': forms.TextInput(attrs={'placeholder': 'Enter Your Name'})
        }


        help_texts = {
            'title': 'this is the title'
        }


# inherit forms

class PostCreateForm(PostForm):
    pass

class PostEditForm(PostForm):
    pass

class PostDeleteForm(PostForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


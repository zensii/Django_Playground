from django import forms

from Exam_Prep_3.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Put an attractive and unique title..." }),
            'content': forms.Textarea(attrs={'placeholder': "Share some interesting facts about your adorable pets..."}),
        }
        # error_messages = {
        #     'title': {
        #         'unique': "Oops! That title is already taken. How about something fresh and fun?",
        #     },
        # }
        # help_texts = {
        #     'image_url': "Share your funniest furry photo URL!",
        # }


class PostDeleteForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):

        widgets = {
            'title': forms.TextInput(attrs={'readonly': 'readonly'}),
            'image_url': forms.TextInput(attrs={'readonly': 'readonly'}),
            'content': forms.Textarea(attrs={'readonly': 'readonly'}),
        }

from django import forms
from django.core.exceptions import ValidationError


class PersonForm(forms.Form):
    STATUS_CHOICE = (
        ('', 'select an option'),
        (1, 'draft'),
        (2, 'published'),
        (3, 'archived'),
    )
    person_name = forms.CharField(
        required=True,
        max_length=10,
        label='Please enter your name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}), # can have many widget attrs
        disabled=False,
        error_messages=(
            {'required': 'Entering your name is required'}  # a way to display custom messages for specific validation errors
        ),

    )

    age = forms.IntegerField(
        required=False,
        label='',
    )

    image = forms.ImageField(required=False)

    is_student = forms.BooleanField()

    # status = forms.ChoiceField(
    #     choices=STATUS_CHOICE,
    #     help_text='select option',
    #     initial='',
    # )                              #this will save the STATUS_CHOICE as a string

    status = forms.IntegerField(
        widget= forms.Select(choices=STATUS_CHOICE),  # the widget is the way we represent the field in HTML
        initial=''

    )                               # This will save the choice as an integer

    email = forms.EmailField()

    password = forms.CharField(
        help_text='Please enter your password.',
        widget=forms.PasswordInput(),

    )


    comment = forms.CharField(
        widget=forms.Textarea()
    )

    radio_button = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=STATUS_CHOICE,
    )

    checkbox_button = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=((1,'option 1'), (2, 'option 2')),
        initial = None,
    )

    date_of_birth = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'datepicker'}),
        label="Select Date of Birth"
    )

    def clean_status(self):
        data = self.cleaned_data['status']
        if data == '':  # Ensuring a valid selection
            raise ValidationError("Please select a valid status.")
        return data

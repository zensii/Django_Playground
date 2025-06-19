from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models
from django.db.models import PositiveIntegerField


# Create your models here.

class Author(models.Model):

    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            RegexValidator(r'^[a-zA-Z]+$', "Your name must contain letters only!")
        ]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            RegexValidator(r'^[a-zA-Z]+$', "Your name must contain letters only!")
        ]
    )
    passcode = models.CharField(
        validators=[ # regex exactly 6 digits
            RegexValidator(r'^\d{6}$', "Your passcode must be exactly 6 digits!"),
        ],
        help_text="Your passcode must be a combination of 6 digits",
    )
    pets_number = models.PositiveIntegerField()
    info = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)


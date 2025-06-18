from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(
                limit_value=2
            ),
            RegexValidator(
                regex=r'^[a-zA-Z0-9_]+$',
                message="Ensure this value contains only letters, numbers, and underscore."
            ),
        ],
    )

    email = models.EmailField()

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(
                limit_value=0,
                message="Age cannot be below 0."
            ),
        ],
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
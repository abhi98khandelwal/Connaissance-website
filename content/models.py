from django.db import models
from django.core.exceptions import ValidationError


class WEvent(models.Model):

    def validate_file_extension(value):
        if not value.name.endswith('.pdf'):
            raise ValidationError(u'Error message')

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=10)
    docfile = models.FileField(upload_to='uploads/%Y/%m/%d', validators=[validate_file_extension])


class PEvent(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=10)
    image = models.ImageField(upload_to='pictures/')

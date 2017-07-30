from django import forms
from django.forms import ModelForm
from .models import PEvent, WEvent
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.conf import settings
import re, os
from PIL import Image


class PhotoForm(ModelForm):
    image = forms.ImageField(label='Upload a Image', required=True, widget=forms.FileInput)

    class Meta:
        model = PEvent
        fields = ['image','name','email', 'contact']

    def __init__(self,*args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PhotoForm,self).clean()
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        contact = self.cleaned_data.get('contact')


        try:
            validate_email(email)
        except:
            raise forms.ValidationError('Not a valid email address!')

        if PEvent.objects.filter(name = name).exists():
            raise forms.ValidationError('Photo with that name already exists!')

    def save(self, commit=True):
        profile = super(PhotoForm,self).save(commit=False)
        profile.save()
        cleaned_data = super(PhotoForm,self).clean()

        image = self.cleaned_data.get('image')
        image.save(settings.MEDIA_ROOT + 'pictures/' + image.name)
        return profile

class WriteForm(ModelForm):
    docfile = forms.FileField(label='Upload PDF', required=True, widget=forms.FileInput)

    class Meta:
        model = WEvent
        fields = ['docfile','name','email', 'contact']

    def __init__(self,*args, **kwargs):
        super(WriteForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(WriteForm, self).clean()
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        contact = self.cleaned_data.get('contact')


        try:
            validate_email(email)
        except:
            raise forms.ValidationError('Not a valid email address!')

        if WEvent.objects.filter(name=name).exists():
            raise forms.ValidationError('File with that name already exists!')

    def save(self, commit=True):
        profile = super(WriteForm,self).save(commit=False)
        profile.save()
        cleaned_data = super(WriteForm,self).clean()

        docfile = self.cleaned_data.get('docfile')
        docfile.save(settings.MEDIA_ROOT + 'uploads/%Y/%m/%d' + docfile.name)
        return profile
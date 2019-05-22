from django.forms import ModelForm
from .models import UserFileUpload
from django import forms

class UploadFileForm(ModelForm):
    class Meta:
        model = UserFileUpload
        fields = ['upload']
        # widgets={
        #         "upload": forms.ClearableFileInput(
        #             attrs={
        #                 'placeholder':'Choose file...',
        #                 'class':'custom-file-label',
        #                 'type':'file',

        #             }
        #         )
        # }